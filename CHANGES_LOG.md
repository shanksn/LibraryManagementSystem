# Changes Log
## Library Management System

**Date**: December 19, 2024

---

## Bug Fixes

### 1. Fixed: Delete Book Bug - Prevent Re-deleting Already Deleted Books

**Problem**: In the deleted books section (when filter is set to "Deleted"), clicking "Delete Book" on an already deleted book would attempt to delete it again without showing any error.

**Solution**: Added validation check before deletion:
```python
# Check if book is already deleted
cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND record_status='Deleted'", (title, author))
deleted_count = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s", (title, author))
total_count = cur.fetchone()[0]

if deleted_count > 0 and deleted_count == total_count:
    conn.close()
    messagebox.showerror("Error", f"Cannot delete '{title}' by {author}.\n\nThis book is already deleted.")
    return
```

**Result**: System now shows error message: "Cannot delete '[Book Title]' by [Author]. This book is already deleted."

**File Modified**: [admin.py](admin.py) (lines 340-349)

---

## New Features

### 2. Added: Defaulters List - Track Overdue Books

**Feature**: New button "Defaulters List" added to Admin Dashboard that displays all members who have overdue books.

**Details**:
- Shows members with books past their due date (15 days from issue date)
- Displays: Member Name, Email, Phone, Book Title, Author, Due Date, Days Overdue
- Calculates days overdue automatically
- Shows "No overdue books found!" message if no defaulters exist
- Window size: 900x500 pixels
- Prevents duplicate windows (brings existing window to front if already open)

**Implementation**:
```python
def defaulters_list():
    # Get all issued books
    # Calculate due date (issue_date + 15 days)
    # Check if due_date < today
    # Display overdue books with member details
```

**Columns Displayed**:
| Column | Width | Description |
|--------|-------|-------------|
| Member Name | 120px | Full name of member |
| Email | 150px | Email address (or 'N/A') |
| Phone | 100px | Phone number (or 'N/A') |
| Book Title | 180px | Title of overdue book |
| Author | 120px | Author name |
| Due Date | 90px | Date book was due (dd/mm/yyyy) |
| Days Overdue | 100px | Number of days past due date |

**File Modified**: [admin.py](admin.py)
- Added to open_windows tracking (line 21)
- Function added (lines 100-156)
- Button added to dashboard (line 477, 487)

**UI Layout**:
- Admin Dashboard now has 5 buttons arranged in 3-column grid:
  - Row 0: Add Member, Add Book
  - Row 1: Search Catalog, Weekly Reports, Defaulters List

**Optional Icon**:
- Icon file path: `images/defaulters_list.png` (50x50 pixels)
- Graceful fallback: Button works without icon if file not present

---

### 3. Added: Prevent Issuing Books to Defaulters

**Feature**: System now validates that members do not have overdue books before allowing new book issues.

**Details**:
- Checks all currently issued books for the member
- Calculates if any book is past its due date (15 days from issue)
- Blocks new book issue if member has any overdue books
- Shows detailed error message listing all overdue books with days overdue

**Error Message Format**:
```
Cannot issue book to '[username]'.

Member has overdue books:
[Book Title] by [Author] (X days overdue)
[Book Title] by [Author] (Y days overdue)

Please return overdue books first.
```

**File Modified**: [admin.py](admin.py) (lines 367-382)

---

### 4. Added: Visual Indicator for Overdue Books in Member Portal

**Feature**: Overdue books in the member's "My Borrowed Books" section are now highlighted in red with a warning legend.

**Details**:
- Overdue books (past due date) are highlighted with light red background (#ffcccc)
- Warning legend appears automatically when overdue books exist
- Legend text: "⚠ Red highlighted books are overdue. Please contact admin."
- Legend styled with red background and bold text for visibility
- Legend is hidden when no overdue books exist

**Implementation**:
- Uses Treeview tags to apply background color
- Calculates overdue status by comparing due_date with current date
- Dynamic legend visibility based on overdue status

**File Modified**: [member.py](member.py) (lines 15-52, 123-126)

---

### 5. Added: View Users Feature

**Feature**: New button "View Users" added to Admin Dashboard to display all system users with their details.

**Details**:
- Displays all users (both admin and member types)
- Shows: Username, User Type, Date Added, Email, Phone
- Sorted by creation date (newest first)
- Uses LEFT JOIN to show admin users without member profiles
- Window size: 900x500 pixels
- Prevents duplicate windows (brings existing window to front if already open)

**Columns Displayed**:
| Column | Width | Description |
|--------|-------|-------------|
| Username | 150px | User's login username |
| User Type | 100px | Admin or Member |
| Date Added | 150px | Account creation date/time (dd/mm/yyyy HH:MM) |
| Email | 250px | Email address (or 'N/A') |
| Phone | 150px | Phone number (or 'N/A') |

**UI Layout Update**:
- Admin Dashboard now has 6 buttons arranged in 3x2 grid:
  - Row 0: Add Member, Add Book, View Users
  - Row 1: Search Catalog, Weekly Reports, Defaulters List

**File Modified**: [admin.py](admin.py)
- Added to open_windows tracking (line 22)
- Function added (lines 159-202)
- Button added to dashboard (line 538, 551)

**Optional Icon**:
- Icon file path: `images/view_users.png` (50x50 pixels)
- Graceful fallback: Button works without icon if file not present

---

## Technical Details

### Database Queries Used

**Defaulters List Query**:
```sql
SELECT b.title, b.author, b.issue_date, m.name, m.email, m.phone, b.book_id
FROM books b
JOIN members m ON b.issued_to_member_id = m.member_id
WHERE b.book_status = 'Issued' AND b.issue_date IS NOT NULL
```

**Delete Book Validation Queries**:
```sql
-- Check if already deleted
SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND record_status='Deleted'

-- Get total count
SELECT COUNT(*) FROM books WHERE title=%s AND author=%s
```

**Prevent Issuing to Defaulters Query**:
```sql
-- Get all issued books for member
SELECT title, author, issue_date
FROM books
WHERE issued_to_member_id = %s AND book_status = 'Issued'
```

**Member Portal Overdue Check Query**:
```sql
-- Get all issued books for current member
SELECT book_id, title, author, year, issue_date
FROM books
WHERE issued_to_member_id = %s AND book_status = 'Issued'
```

**View Users Query**:
```sql
-- Get all users with member details (if available)
SELECT u.username, u.user_type, u.created_date, m.email, m.phone
FROM users u
LEFT JOIN members m ON u.user_id = m.user_id
ORDER BY u.created_date DESC
```

### Due Date Calculation Logic

```python
due_date = issue_date + timedelta(days=15)
if due_date < today:
    days_overdue = (today - due_date).days
```

---

## Testing Checklist

**Bug Fix Testing**:
- [x] Set filter to "Deleted"
- [x] Select a deleted book
- [x] Click "Delete Book"
- [x] Verify error message appears
- [x] Verify book is NOT deleted again

**Defaulters List Testing**:
- [x] Click "Defaulters List" button
- [x] Window opens showing overdue books
- [x] Verify all columns display correctly
- [x] Verify days overdue calculation is correct
- [x] Test with no overdue books (shows success message)
- [x] Test duplicate window prevention

**Prevent Issuing to Defaulters Testing**:
- [ ] Issue a book to a member with overdue books
- [ ] Verify error message displays with list of overdue books
- [ ] Verify new book is NOT issued
- [ ] Return overdue book and verify member can now borrow

**Member Portal Overdue Highlighting Testing**:
- [ ] Login as member with overdue books
- [ ] Verify overdue books have red background (#ffcccc)
- [ ] Verify legend appears with warning message
- [ ] Return overdue book and verify highlighting disappears
- [ ] Verify legend is hidden when no overdue books exist

---

## Code Quality

**Principles Followed**:
- Simple and concise code
- Consistent with existing codebase style
- Proper error handling
- Graceful fallbacks for missing resources
- Prevents duplicate windows
- Clear variable names
- Appropriate comments

---

## User Documentation Updates Needed

The following sections should be updated in the User Manual:

1. **Admin Dashboard Overview** - Add Defaulters List button description
2. **Administrator Workflows** - Add new section 4.8: "Viewing Defaulters List"
3. **Troubleshooting** - Add "Issue: Cannot delete book - Already deleted"
4. **Screenshot Placeholders** - Add screenshot for Defaulters List window

---

## Version History Update

Add to version history:
```
| Version | Date | Changes |
|---------|------|---------|
| 3.2 | Dec 2024 | Fixed delete bug, Added Defaulters List feature |
```

---

**End of Changes Log**
