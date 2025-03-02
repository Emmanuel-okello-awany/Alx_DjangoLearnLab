This an introductory projecct to Django 
# LibraryProject

This is a Django project created for learning Django development. It serves as a base for future Django applications.

## Installation
1. Install Django:

# Django Permissions and Groups Implementation

## Overview
This Django project demonstrates role-based access control using Django's built-in permissions and groups.

## Features
- Users are assigned to **Viewers, Editors, or Admins** groups.
- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) are defined in `Article` model.
- Users are restricted from certain actions based on their group.

## User Permissions
| Role    | Can View | Can Create | Can Edit | Can Delete |
|---------|---------|------------|---------|------------|
| Viewers | ✅      | ❌         | ❌      | ❌         |
| Editors | ✅      | ✅         | ✅      | ❌         |
| Admins  | ✅      | ✅         | ✅      | ✅         |

## Setup Instructions
1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
