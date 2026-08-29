# NetSphere Pro — ISP Management Dashboard

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blueviolet)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

> **A complete, enterprise-grade ISP management platform with a pure black glassmorphism UI.**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Login Credentials](#-login-credentials)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview

**NetSphere Pro** is a full-featured Internet Service Provider (ISP) management dashboard designed to streamline operations, manage customers, handle billing, track network infrastructure, and provide real-time analytics — all wrapped in a sleek, pure black glassmorphism theme.

Built with vanilla HTML, CSS, and JavaScript, it runs entirely in the browser with localStorage persistence, making it perfect for small to medium ISPs looking for a lightweight yet powerful management solution.

---

## ✨ Features

### 🔐 Authentication & Role-Based Access
- **Admin** — Full system control
- **Customer** — Personal dashboard with limited access
- Secure login with role switching

### 📊 Dashboard (Admin)
- **Key Metrics** — Total customers, active connections, open tickets, total revenue
- **Revenue Trend Chart** — 6-month revenue visualization
- **Package Distribution Chart** — Doughnut chart showing subscriber breakdown
- **Recent Payments** — Latest invoice activity
- **System Snapshot** — Quick overview of packages, pending invoices, staff, and system status

### 👥 Customer Management
- **Add / Edit / Delete** customers
- **Search** by name or email
- **Filter** by package type or status
- **Bulk Selection** — Delete multiple customers at once
- **Bulk Import** — Upload CSV files with customer data
- **Export CSV** — Download customer list
- **Pagination** — 5 customers per page

### 📦 Package Management
- Create, edit, and delete internet packages
- Display package name, speed, and monthly price
- Clean card-based UI

### 💰 Billing & Invoices
- **Create invoices** with customer, amount, due date, and status
- **Mark invoices as paid** with one click
- **Download PDF invoices** (jsPDF integration)
- **Delete invoices**
- **Auto-billing** — Unpaid invoices automatically become overdue

### 🎫 Support Tickets
- **Create tickets** with subject and priority (Low / Medium / High)
- **Toggle status** — Open / Closed
- **Delete tickets**
- Ticket priority badges (High = red, Medium = yellow, Low = purple)

### 👔 Staff Management
- Add, edit, and delete staff members
- Roles: Technician, Support Lead, Billing Specialist, Manager
- Status tracking (Active / Inactive)

### 🌐 Network Operations
- **Network Topology** — Visual representation of routers, switches, and access points with live status indicators
- **IP Pool Management** — Track total, available, and assigned IPs with a visual grid
- **Router / ONU Status** — Device name, type, MAC, firmware, uptime, and status
- **Bandwidth Usage** — Total usage, monthly cap, progress bar, and daily usage chart
- **Outage Dashboard** — Active outages with severity levels (Critical, Major, Minor)

### 📈 Reports & Analytics
- **Total Revenue** and **Customer Growth** metrics
- **Revenue Over Time** — Monthly bar chart
- **Customer Growth** — Monthly line chart
- **Export PDF Report** — Generate a summary report

### 🗺️ Customer Locations
- **Leaflet.js** integration
- **Live customer positions** mapped with color-coded markers
- Green = Online, Red = Offline
- Popup with customer details (name, package, status, data used)

### ❓ Help Center
- FAQ section with expandable answers
- **Search** functionality to filter FAQs

### 📝 Activity Logs
- **Audit trail** of all user actions
- Time, user, action, and details
- **Clear Logs** button

### 👤 Customer Portal
- **My Dashboard** — Package info, due amount, ticket count, data usage
- **Bandwidth Usage Chart** — Last 7 days
- **Recent Activity** — Invoices and tickets
- **My Profile** — View and change package
- **My Payments** — Payment history with "Pay Now" button
- **My Tickets** — Support ticket history
- **Submit Ticket** — Create a new support ticket

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **HTML5** | Structure |
| **CSS3** | Styling & Glassmorphism |
| **JavaScript (ES6)** | Functionality & Logic |
| **Chart.js 4** | Charts & Graphs |
| **jsPDF 2.5** | PDF Invoice & Report Export |
| **Leaflet.js 1.9** | Interactive Map |
| **Font Awesome 6** | Icons |
| **Google Fonts (Inter)** | Typography |
| **localStorage** | Data Persistence |

---

## 📥 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/netsphere-pro.git
cd netsphere-pro
