# Database Relationships
## Library Management System

**Class XII Computer Science Project**
**Student**: Jhanvi Shankar

---

## Primary and Foreign Key Relationships

| Table | Primary Key | Foreign Key(s) | References |
|-------|-------------|----------------|------------|
| **users** | user_id | None | - |
| **members** | member_id | user_id | users(user_id) |
| **books** | book_id | issued_to_member_id | members(member_id) |
| **transactions** | transaction_id | book_id<br>member_id<br>admin_user_id | books(book_id)<br>members(member_id)<br>users(user_id) |

---

## Relationship Summary

| From Table | To Table | Relationship Type | Description |
|------------|----------|-------------------|-------------|
| users | members | One-to-One | Each member has one user account |
| members | books | One-to-Many | One member can have multiple books issued |
| books | transactions | One-to-Many | One book can have multiple transactions |
| members | transactions | One-to-Many | One member can have multiple transactions |
| users | transactions | One-to-Many | One admin user can perform multiple transactions |

---

## Entity Relationship Diagram (Text Format)

```
┌─────────────────┐
│     users       │
│─────────────────│
│ PK: user_id     │
│     username    │
│     password    │
│     full_name   │
│     user_type   │
│     status      │
└────────┬────────┘
         │
         │ 1:1
         │
         ▼
┌─────────────────┐         ┌─────────────────┐
│    members      │         │     books       │
│─────────────────│         │─────────────────│
│ PK: member_id   │◄────────│ PK: book_id     │
│ FK: user_id     │   1:M   │     title       │
│     name        │         │     author      │
│     address     │         │     isbn        │
│     email       │         │     year        │
│     phone       │         │     copy_number │
└────────┬────────┘         │     book_status │
         │                  │ FK: issued_to   │
         │                  │     _member_id  │
         │                  └────────┬────────┘
         │                           │
         │         ┌─────────────────┘
         │         │
         │  1:M    │  1:M
         │         │
         └────┐    │
              ▼    ▼
       ┌──────────────────┐
       │   transactions   │
       │──────────────────│
       │ PK: transaction  │
       │     _id          │
       │ FK: book_id      │
       │ FK: member_id    │
       │ FK: admin_user   │
       │     _id          │
       │     action       │
       │     transaction  │
       │     _date        │
       │     notes        │
       └──────────────────┘
            ▲
            │
            │ 1:M
            │
┌───────────┴─────┐
│     users       │
│  (as admin)     │
└─────────────────┘
```

---

## Detailed Field Relationships

### users → members
- **Relationship**: One user account maps to one member profile
- **Foreign Key**: members.user_id → users.user_id
- **Purpose**: Links member profile to their login credentials
- **Constraint**: CASCADE (when user deleted, member profile also deleted)

### members → books
- **Relationship**: One member can have multiple books issued simultaneously
- **Foreign Key**: books.issued_to_member_id → members.member_id
- **Purpose**: Tracks which member currently has a book
- **Constraint**: NULL allowed (book not issued to anyone)

### books → transactions
- **Relationship**: One book can have multiple transaction records over time
- **Foreign Key**: transactions.book_id → books.book_id
- **Purpose**: Maintains audit trail of all book operations
- **Constraint**: NULL allowed (transactions for adding books may not have book_id initially)

### members → transactions
- **Relationship**: One member can have multiple transactions
- **Foreign Key**: transactions.member_id → members.member_id
- **Purpose**: Tracks all member-related activities
- **Constraint**: NULL allowed (some transactions may not involve members)

### users → transactions
- **Relationship**: One admin user can perform multiple transactions
- **Foreign Key**: transactions.admin_user_id → users.user_id
- **Purpose**: Tracks which admin performed each action
- **Constraint**: NULL allowed (system-generated transactions)

---

## Referential Integrity Rules

1. **Cannot delete a user** if they have an associated member profile (must delete member first)
2. **Cannot delete a member** if they have books currently issued (must return books first)
3. **Cannot delete a book** that has transaction history (soft delete used instead)
4. **Transactions are immutable** - once created, they serve as permanent audit trail

---

## Key Constraints Summary

| Table | Unique Constraints | Not Null Constraints |
|-------|-------------------|---------------------|
| **users** | username | username, password, full_name, user_type |
| **members** | None | name (only) |
| **books** | None | title, author, isbn, year, copy_number |
| **transactions** | None | action (only) |

---

**End of Document**
