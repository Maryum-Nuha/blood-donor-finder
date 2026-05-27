# 🩸 Blood Donor Finder System

A lightweight, secure, and user-friendly web application built with **Flask** and **SQLite3** to manage and find blood donors. This system allows authorized users to manage donor registries, perform fast searches based on blood group requirements, and maintain crucial record modifications securely.

---

## 🚀 Features

*   **Secure Authentication:** Protected administrative portal preventing unauthorized donor directory manipulation.
*   **Donor Onboarding Form:** Simple input panel on the home dashboard to log fresh donor profiles with native 10-digit phone validations.
*   **Targeted Search Tool:** Dedicated interface allowing instant filtering of profiles based on requested blood groups.
*   **Full CRUD Management:** View a master table of all registered donors with native permissions to **Edit** user info or **Delete** invalid entries.
*   **Local Engine Data:** Zero external cloud dependencies; runs a lightweight self-contained SQL database wrapper locally (`donors.db`).

---

## 📁 Directory Structure

Ensure your project folders align with this classic Flask directory layout to allow the static routing and templates to bind correctly:

```text
blood-donor-finder/
│
├── app.py                 # Core application logic and routing configurations
├── donors.db              # Local SQLite database instance (automatically created)
│
├── static/
│   └── style.css          # Frontend layout aesthetic, responsive box structures
│
└── templates/
    ├── login.html         # Admin access authentication gateway
    ├── index.html         # Home portal featuring the onboarding form
    ├── search.html        # Dynamic database querying display
    ├── donors.html        # Central master list showing all records 
    └── edit.html          # Individual record updating form
    # blood-donor-finder