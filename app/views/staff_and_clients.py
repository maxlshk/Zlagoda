from app.views.main import generate_phone_number, generate_unique_id, generate_unique_upc
from flask import Blueprint, render_template
import random


staff_and_clients = Blueprint('staff_and_clients', __name__)


@staff_and_clients.route('/workers')
def workers():
    active_tab = 'workers'
    positions = ["Manager", "Cashier", "Cleaner", "Consultant", "Security"]
    people = [
        {
            "name": f"Worker {i}",
            "id": generate_unique_id(),
            "position": random.choice(["Manager", "Cashier", "Cleaner", "Consultant", "Security"]),
            "salary": f"${random.uniform(500, 900):.0f}",
            "employment_date": f"2021-{random.randint(10, 12)}-{random.randint(10, 28)}",
            "birth_date": f"{random.randint(1980, 2005)}-{random.randint(10, 12)}-{random.randint(10, 28)}",
            "phone_number": generate_phone_number(),
            "address": f"City, Street, {random.randint(1, 100)}",
        } for i in range(1, 13)
    ]
    return render_template('pages/staff_and_clients.html', active_tab=active_tab, positions=positions, people=people)


@staff_and_clients.route('/customers')
def clients():
    people = [
        {
            "name": f"Customer {i}",
            "card number": generate_unique_id(),
            "percent": f"{random.randint(1, 100)}%",
            "phone_number": generate_phone_number(),
            "address": f"City, Street, {random.randint(1, 100)}",
        } for i in range(1, 21)
    ]
    active_tab = 'clients'
    return render_template('pages/staff_and_clients.html', people=people, active_tab=active_tab)
