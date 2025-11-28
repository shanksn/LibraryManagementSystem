#!/usr/bin/env python3
"""
Test Script: Set a user to inactive status and test login
Library Management System - Class XII Project
"""

import mysql.connector
from config import db_config

def show_users():
    """Display all users and their current status"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, username, full_name, user_type, status FROM users ORDER BY user_id")
    users = cursor.fetchall()

    print("\n" + "="*80)
    print("CURRENT USERS IN DATABASE")
    print("="*80)
    print(f"{'ID':<5} {'Username':<15} {'Full Name':<20} {'Type':<10} {'Status':<10}")
    print("-"*80)

    for user in users:
        print(f"{user[0]:<5} {user[1]:<15} {user[2]:<20} {user[3]:<10} {user[4]:<10}")

    print("="*80 + "\n")
    conn.close()

def set_user_inactive(username):
    """Set a specific user to inactive status"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Check if user exists
    cursor.execute("SELECT user_id, full_name, status FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if not user:
        print(f"❌ User '{username}' not found!")
        conn.close()
        return False

    current_status = user[2]
    print(f"\n📝 User: {user[1]} (username: {username})")
    print(f"   Current Status: {current_status}")

    if current_status == 'inactive':
        print(f"   ⚠️  User is already inactive!")
        conn.close()
        return True

    # Set user to inactive
    cursor.execute("UPDATE users SET status = 'inactive' WHERE username = %s", (username,))
    conn.commit()

    print(f"   ✅ User status changed to: inactive")
    conn.close()
    return True

def set_user_active(username):
    """Set a specific user to active status"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Update user status
    cursor.execute("UPDATE users SET status = 'active' WHERE username = %s", (username,))
    conn.commit()

    print(f"✅ User '{username}' restored to active status")
    conn.close()

if __name__ == '__main__':
    print("\n" + "🔧 INACTIVE USER TEST SCRIPT".center(80))
    print("="*80)

    # Show all users before
    print("\n1️⃣  BEFORE: Current users in database")
    show_users()

    # Set 'anjali' to inactive for testing
    test_user = 'anjali'
    print(f"\n2️⃣  Setting user '{test_user}' to INACTIVE status...")
    set_user_inactive(test_user)

    # Show all users after
    print(f"\n3️⃣  AFTER: Updated user status")
    show_users()

    print("\n" + "="*80)
    print("🧪 TEST INSTRUCTIONS:")
    print("="*80)
    print(f"1. Run the login application: python3 login.py")
    print(f"2. Try to login with:")
    print(f"   Username: {test_user}")
    print(f"   Password: {test_user}123")
    print(f"3. You should see: 'Account is inactive. Please contact administrator.'")
    print(f"4. Try logging in with an active user (e.g., priya/priya123) - should work")
    print("="*80)

    print(f"\n💡 TO RESTORE '{test_user}' TO ACTIVE:")
    print(f"   Run: python3 -c \"from test_inactive_user import set_user_active; set_user_active('{test_user}')\"")
    print(f"   Or manually: UPDATE users SET status='active' WHERE username='{test_user}';")
    print("\n")
