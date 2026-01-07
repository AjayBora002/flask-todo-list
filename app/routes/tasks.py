from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
@login_required
def view_tasks():
    sort_by = request.args.get('sort_by', 'due_date')
    
    # Only fetch tasks belonging to the current user
    tasks = Task.query.filter_by(user_id=current_user.id).all()

    if sort_by == 'priority':
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        tasks.sort(key=lambda x: priority_order.get(x.priority, 3))
    elif sort_by == 'due_date':
        tasks.sort(key=lambda x: (x.due_date is None, x.due_date))

    return render_template('tasks.html', tasks=tasks, sort_by=sort_by)

@tasks_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    priority = request.form.get('priority')
    due_date_str = request.form.get('due_date')
    
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            pass

    if title:
        # Create task linked to current_user
        new_task = Task(
            title=title, 
            status='Pending', 
            priority=priority, 
            due_date=due_date,
            author=current_user 
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
@login_required
def toggle_status(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Ensure user owns the task
    if task.user_id != current_user.id:
        flash('You do not have permission to modify this task.', 'danger')
        return redirect(url_for('tasks.view_tasks'))

    if task.status == 'Pending':
        task.status = 'Working'
    elif task.status == 'Working':
        task.status = 'Done'
    else:
        task.status = 'Pending'
    db.session.commit()

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>', methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    # Ensure user owns the task before deleting
    if task.user_id != current_user.id:
        flash('You do not have permission to delete this task.', 'danger')
        return redirect(url_for('tasks.view_tasks'))

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted.', 'success')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods=["POST"])
@login_required
def clear_tasks():
    # Only delete current user's tasks
    Task.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('All your tasks cleared!', 'info')

    return redirect(url_for('tasks.view_tasks'))