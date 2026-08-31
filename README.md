# 🌐 NetSphere Pro — ISP Management System

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?logo=javascript\&logoColor=black)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4.0-FF6384)
![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-199900)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen)

> **A modern, feature-rich ISP management dashboard for managing customers, internet packages, billing, network infrastructure, IP resources, support tickets, outages, reports, and customer services.**

---

## 📋 Table of Contents

* [Overview](#-overview)
* [Key Features](#-key-features) 
* [Technology Stack](#️-technology-stack)
* [System Modules](#-system-modules)
* [User Roles](#-user-roles)
* [Network Management](#-network-management)
* [Billing & Payments](#-billing--payments)
* [Reports & Analytics](#-reports--analytics)
* [Customer Portal](#-customer-portal)
* [Security Considerations](#-security-considerations)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Demo Credentials](#-demo-credentials)
* [Data Storage](#-data-storage)
* [Development Roadmap](#-development-roadmap)
* [Contributing](#-contributing)
* [License](#-license)
* [Project Information](#-project-information)

---

## 🚀 Overview

**NetSphere Pro** is a browser-based **Internet Service Provider (ISP) Management System** designed to centralize and simplify common ISP operations through a single management dashboard.

The system provides modules for:

* Customer management
* Internet package management
* Billing and invoices
* Support ticket management
* Staff management
* Network infrastructure monitoring
* IP pool management
* Bandwidth usage tracking
* Outage management
* Reports and analytics
* Customer location management
* Activity logging
* Customer self-service

NetSphere Pro is built using **vanilla HTML5, CSS3, and JavaScript (ES6)** with a responsive **black glassmorphism user interface**.

The current version operates entirely in the browser and uses **localStorage** for data persistence, making it lightweight and easy to run without a backend server.

> **Project Status:** The current version is a frontend-focused ISP management system/prototype. Backend services, database integration, and direct network-device integration are planned for future development.

---

# ✨ Key Features

## 🔐 Authentication & Role-Based Access

NetSphere Pro provides separate interfaces for different user roles.

### Admin

Administrators can manage:

* Customers
* Internet packages
* Billing and invoices
* Staff
* Network infrastructure
* IP resources
* Outages
* Reports
* Support tickets
* Activity logs
* System operations

### Customer

Customers have access to their own service information, including:

* Personal dashboard
* Internet package
* Payments
* Invoices
* Bandwidth usage
* Support tickets
* Profile information

---

# 📊 Dashboard

The administrative dashboard provides an overview of important ISP operations.

### Dashboard Metrics

* Total customers
* Active connections
* Open support tickets
* Total revenue
* Internet packages
* Pending invoices
* Staff information
* System status

### Analytics

The dashboard includes interactive visualizations for:

* Revenue trends
* Package distribution
* Customer statistics
* Recent payment activity

---

# 👥 Customer Management

The customer management module allows administrators to manage ISP subscribers.

### Features

* Add customers
* Edit customer information
* Delete customers
* Search customers
* Filter customers
* Filter by package
* Filter by connection status
* Select multiple customers
* Bulk delete
* Import customers using CSV
* Export customer information to CSV
* Pagination

This module provides a centralized interface for maintaining subscriber information.

---

# 📦 Internet Package Management

Administrators can create and manage ISP service packages.

### Package Information

Each package can contain:

* Package name
* Internet speed
* Monthly price
* Subscriber information

### Package Operations

* Create packages
* Edit packages
* Delete packages
* View package information

Packages are displayed using a responsive card-based interface.

---

# 💰 Billing & Invoices

The billing module provides basic invoice management functionality.

### Features

* Create invoices
* Assign invoices to customers
* Set invoice amounts
* Set due dates
* Track invoice status
* Mark invoices as paid
* Delete invoices
* Identify overdue invoices
* Generate PDF invoices

### Invoice Status

Invoices can be categorized as:

* Paid
* Unpaid
* Pending
* Overdue

PDF invoice generation is implemented using **jsPDF**.

---

# 🎫 Support Ticket Management

The support system allows customers and administrators to manage service-related issues.

### Features

* Create support tickets
* Add ticket subjects
* Add ticket descriptions
* Assign priority levels
* Change ticket status
* Close tickets
* Delete tickets
* Track ticket activity

### Priority Levels

| Priority  | Description              |
| --------- | ------------------------ |
| 🔴 High   | Urgent or critical issue |
| 🟡 Medium | Normal service issue     |
| 🟣 Low    | Non-urgent request       |

---

# 👔 Staff Management

Administrators can manage ISP staff members.

### Supported Roles

* Technician
* Support Lead
* Billing Specialist
* Manager

### Staff Features

* Add staff members
* Edit staff information
* Delete staff members
* Assign staff roles
* Track active/inactive status

---

# 🌐 Network Management

Network management is one of the main components of NetSphere Pro.

The system provides interfaces for monitoring and managing common ISP network resources.

## 🗺️ Network Topology

The network topology module provides a visual representation of network infrastructure, including:

* Routers
* Switches
* Access Points

Network devices can display operational states such as:

* 🟢 Online
* 🔴 Offline

The topology interface is designed to provide administrators with a simplified visual overview of the network infrastructure.

---

## 🌐 IP Pool Management

The IP Pool Management module provides an interface for tracking IP address resources.

IP addresses can be represented according to their allocation state:

* Available
* Assigned
* Reserved

The system includes a visual IP pool representation to make IP resource management easier.

---

## 📡 Router & ONU Information

Network devices can display information such as:

* Device name
* Device type
* MAC address
* Firmware version
* Uptime
* Operational status

---

## 📊 Bandwidth Usage

The bandwidth module provides usage information such as:

* Total bandwidth usage
* Monthly usage limit
* Usage percentage
* Progress visualization
* Daily usage statistics

---

# 🚨 Outage Management

The Outage Dashboard provides a centralized interface for monitoring service outages.

### Severity Levels

* 🔴 Critical
* 🟡 Major
* 🟣 Minor

Outage information can include:

* Outage title
* Description
* Severity
* Time
* Current status

This allows administrators to maintain an overview of ongoing service disruptions.

---

# 📈 Reports & Analytics

The reporting module provides analytical information about ISP operations.

### Available Metrics

* Total revenue
* Customer growth
* Monthly revenue
* Customer statistics
* Package distribution

### Charts

The system provides visualizations for:

* Revenue over time
* Customer growth
* Package distribution
* Bandwidth usage

### PDF Reports

Summary reports can be exported as PDF documents using **jsPDF**.

---

# 🗺️ Customer Location Management

NetSphere Pro integrates **Leaflet.js** for interactive customer location visualization.

The map can display customer information such as:

* Customer location
* Customer name
* Internet package
* Connection status
* Data usage

### Connection Indicators

🟢 **Green** — Online

🔴 **Red** — Offline

This provides administrators with a geographic overview of customer/service distribution.

---

# ❓ Help Center

The Help Center provides frequently asked questions and answers.

### Features

* FAQ categories
* Expandable answers
* FAQ search
* Dynamic filtering
* Responsive interface

---

# 📝 Activity Logs

NetSphere Pro includes an activity logging interface for tracking system actions.

Activity information can include:

* Timestamp
* User
* Action
* Details

Administrators can also clear the activity log.

> **Note:** Because the current implementation stores data in browser localStorage, these logs should not be considered tamper-proof audit records. A production implementation should store audit logs securely on the backend.

---

# 👤 Customer Portal

The Customer Portal provides customers with access to their own service information.

## 🏠 My Dashboard

Customers can view:

* Current internet package
* Amount due
* Support ticket count
* Bandwidth usage
* Account information

## 📊 Bandwidth Usage

Customers can view recent bandwidth usage through an interactive chart.

## 💳 My Payments

Customers can access:

* Payment history
* Invoice information
* Outstanding payments
* Payment actions

## 🎫 My Tickets

Customers can:

* View existing support tickets
* Create new tickets
* Track ticket status

## 👤 My Profile

Customers can view and manage their service information and package details.

---

# 🎨 User Interface

NetSphere Pro uses a modern **black glassmorphism design** focused on providing a professional network-management experience.

### UI Features

* Pure black theme
* Glassmorphism cards
* Gradient accents
* Responsive layouts
* Interactive components
* Animated elements
* Modal dialogs
* Toast notifications
* Responsive tables
* Dashboard cards
* Modern typography

The interface is designed to provide a clean and consistent experience across the different modules.

---

# 📱 Responsive Design

The application is designed to adapt to different screen sizes.

Responsive functionality includes:

* Responsive sidebar
* Mobile-friendly navigation
* Responsive dashboard cards
* Responsive tables
* Mobile-friendly forms
* Responsive modals
* Responsive package cards
* Mobile-friendly network interfaces

---

# 🛠️ Technology Stack

| Technology               | Purpose                              |
| ------------------------ | ------------------------------------ |
| **HTML5**                | Application structure                |
| **CSS3**                 | Styling, layout and glassmorphism UI |
| **JavaScript ES6**       | Application logic and functionality  |
| **Chart.js 4**           | Charts and data visualization        |
| **jsPDF 2.5**            | PDF invoice and report generation    |
| **Leaflet.js 1.9**       | Interactive maps                     |
| **Font Awesome 6**       | Icons                                |
| **Google Fonts – Inter** | Typography                           |
| **localStorage**         | Browser-side data persistence        |

---

# 🧩 System Modules

The current system consists of the following major modules:

```text
NetSphere Pro
│
├── Authentication
│
├── Admin Dashboard
│   ├── Statistics
│   ├── Revenue Analytics
│   ├── Package Distribution
│   └── Recent Payments
│
├── Customer Management
│   ├── Customer CRUD
│   ├── Search & Filtering
│   ├── CSV Import
│   └── CSV Export
│
├── Package Management
│
├── Billing & Invoices
│
├── Support Tickets
│
├── Staff Management
│
├── Network Operations
│   ├── Network Topology
│   ├── IP Pool
│   ├── Router/ONU Status
│   ├── Bandwidth Usage
│   └── Outage Management
│
├── Reports & Analytics
│
├── Customer Locations
│
├── Activity Logs
│
├── Help Center
│
└── Customer Portal
```

---

# 👥 User Roles

The system is designed around two primary user roles.

| Role         | Access                                  |
| ------------ | --------------------------------------- |
| **Admin**    | Full system management                  |
| **Customer** | Personal service and account management |

The role-based interface is intended to ensure that users see functionality relevant to their responsibilities.

> **Production Note:** True authorization should be enforced server-side in a future backend implementation rather than relying only on frontend role checks.

---

# 💾 Data Storage

The current version uses **browser localStorage** for data persistence.

### Advantages

* No database setup required
* No backend required
* Easy to run locally
* Lightweight
* Suitable for demonstrations and prototypes
* Data can persist between browser sessions

### Limitations

localStorage is not suitable for production ISP operations because:

* Data is stored on the client device
* Users can potentially modify stored data
* There is no centralized database
* Data is not automatically synchronized between users
* It does not provide secure server-side authorization
* It is unsuitable for sensitive customer information at production scale

A future version should migrate to a secure backend and database architecture.

---

# 🔒 Security Considerations

NetSphere Pro is currently a **frontend/browser-based project**.

For educational, demonstration, and portfolio purposes, this architecture is useful. However, it should not be deployed as a production ISP management platform without significant security improvements.

### Recommended Production Security

#### Authentication

* Server-side authentication
* Secure password hashing
* Secure session management
* Multi-factor authentication
* Account lockout/rate limiting

#### Authorization

Implement server-side **Role-Based Access Control (RBAC)**.

Example:

```text
Admin
├── Customer Management
├── Package Management
├── Billing
├── Network Operations
├── Staff Management
└── Reports

Customer
├── My Dashboard
├── My Payments
├── My Tickets
└── My Profile
```

#### Web Application Security

A production implementation should also include:

* Input validation
* Output encoding
* XSS protection
* CSRF protection
* SQL injection prevention
* Secure API design
* Rate limiting
* HTTPS/TLS
* Security headers
* Secure cookies
* Server-side audit logging
* Database backups

---

# 🔮 Future Development

The long-term goal of NetSphere Pro is to evolve from a browser-based prototype into a complete full-stack ISP management platform.

## 🗄️ Backend Integration

Potential backend technologies include:

* Node.js
* Express.js
* Python
* Django
* FastAPI

## 🗃️ Database Integration

Potential database technologies:

* PostgreSQL
* MySQL
* MariaDB

## 🌐 Real Network Integration

Future versions could integrate with actual ISP infrastructure through:

* MikroTik RouterOS API
* SNMP
* RADIUS
* PPPoE
* DHCP
* VLAN management
* Network monitoring systems
* Bandwidth management systems

## 💳 Payment Integration

Future payment functionality could include:

* Online payment gateway
* Automatic payment verification
* Automated invoice generation
* Subscription renewal
* Payment reminders

## 🔔 Notifications

Future notification systems could support:

* Email notifications
* SMS notifications
* Payment reminders
* Service-expiry alerts
* Outage notifications
* Support ticket notifications

## 📡 Advanced Network Monitoring

Potential monitoring features include:

* Real-time bandwidth monitoring
* Router health monitoring
* CPU and memory monitoring
* Packet-loss monitoring
* Latency monitoring
* SNMP statistics
* Network alerts
* Device availability monitoring

---

# 🛣️ Development Roadmap

## Version 1.0 — Current

* [x] Authentication interface
* [x] Admin dashboard
* [x] Customer portal
* [x] Customer management
* [x] Package management
* [x] Billing and invoices
* [x] Support tickets
* [x] Staff management
* [x] Network topology
* [x] IP pool management
* [x] Router/ONU information
* [x] Bandwidth usage
* [x] Outage management
* [x] Reports and analytics
* [x] Customer location map
* [x] Activity logs
* [x] Help center
* [x] CSV import/export
* [x] PDF generation
* [x] Responsive UI
* [x] localStorage persistence

## Version 2.0 — Planned

* [ ] Backend API
* [ ] PostgreSQL/MySQL database
* [ ] Secure server-side authentication
* [ ] Advanced RBAC
* [ ] REST API
* [ ] Real-time network monitoring
* [ ] MikroTik integration
* [ ] RADIUS integration
* [ ] SNMP monitoring
* [ ] Automated billing
* [ ] Payment gateway integration
* [ ] Email notifications
* [ ] SMS notifications
* [ ] Advanced audit logging

---

# 📥 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/netsphere-pro.git
```

## 2. Navigate to the Project

```bash
cd netsphere-pro
```

## 3. Run the Application

You can open the HTML file directly in a modern web browser.

For development, using **Visual Studio Code + Live Server** is recommended.

### Using Live Server

1. Open the project folder in Visual Studio Code.
2. Install the **Live Server** extension.
3. Open the main HTML file.
4. Right-click the file.
5. Select **Open with Live Server**.
6. The application will open in your browser.

---

# 🔑 Demo Credentials

Replace the following with the actual demo credentials used by your project.

### Admin

```text
Username: admin
Password: your-admin-password
```

### Customer

```text
Username: customer
Password: your-customer-password
```

> ⚠️ **Security Notice:** Never commit real passwords, API keys, database credentials, or other secrets to GitHub.

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

### 1. Fork the repository

### 2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

### 4. Commit your changes

```bash
git commit -m "Add new feature"
```

### 5. Push your branch

```bash
git push origin feature/new-feature
```

### 6. Open a Pull Request

Please ensure your contribution is clearly documented and does not introduce security vulnerabilities or sensitive information.

---

# 🐛 Bug Reports & Feature Requests

If you discover a bug or want to suggest a new feature, create an issue in the GitHub repository.

When reporting a bug, provide:

* Problem description
* Steps to reproduce
* Expected behavior
* Actual behavior
* Browser/device information
* Relevant screenshots or logs, when necessary

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

* Use the project
* Modify the project
* Distribute the project
* Use it for educational purposes
* Use it for personal projects

See the `LICENSE` file for complete license terms.

---

# 📌 Project Information

| Information        | Details                            |
| ------------------ | ---------------------------------- |
| **Project Name**   | NetSphere Pro                      |
| **Project Type**   | ISP Management System              |
| **Version**        | 1.0.0                              |
| **Architecture**   | Browser-based frontend application |
| **Frontend**       | HTML5, CSS3, JavaScript ES6        |
| **Data Storage**   | Browser localStorage               |
| **UI Design**      | Black Glassmorphism                |
| **Charts**         | Chart.js                           |
| **Maps**           | Leaflet.js                         |
| **PDF Generation** | jsPDF                              |
| **License**        | MIT                                |
| **Status**         | Active Development                 |

---

# ⭐ Support

If you find **NetSphere Pro** useful or interesting, consider supporting the project:

⭐ Star the repository
🍴 Fork the repository
🐛 Report bugs
💡 Suggest improvements
🤝 Contribute to the project

---

## 🌐 NetSphere Pro

**Manage Customers. Monitor Networks. Simplify ISP Operations.**

> A networking-focused ISP management project designed to bring customer management, billing, network operations, IP management, support, and analytics together in one centralized platform.
