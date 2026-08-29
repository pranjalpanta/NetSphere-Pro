<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>NetSphere Pro — ISP Management</title>
    <!-- Font Awesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <!-- Chart.js 4 -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js">
    </script>
    <!-- jsPDF -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js">
    </script>
    <!-- Leaflet CSS & JS (For Map Feature) -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="">
    </script>
    <!-- Google Fonts: Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
    <style>
        /* ============================================================
           FULL CSS — PURE BLACK GLASSMORPHISM THEME
           ============================================================ */
        :root {
            --bg-primary: #000000;
            --bg-secondary: #0a0a0a;
            --bg-card: rgba(255, 255, 255, 0.03);
            --bg-card-hover: rgba(255, 255, 255, 0.06);
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.06);
            --text-primary: #ffffff;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --accent-1: #6366f1;
            --accent-2: #8b5cf6;
            --accent-3: #06b6d4;
            --accent-gradient: linear-gradient(135deg, #6366f1, #8b5cf6, #06b6d4);
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --shadow-sm: 0 4px 20px rgba(0, 0, 0, 0.6);
            --shadow-md: 0 8px 40px rgba(0, 0, 0, 0.7);
            --shadow-lg: 0 20px 60px rgba(0, 0, 0, 0.8);
            --shadow-glow: 0 0 40px rgba(99, 102, 241, 0.06);
            --radius: 16px;
            --radius-sm: 10px;
            --radius-xs: 8px;
            --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --sidebar-width: 260px;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: var(--font);
            background: var(--bg-primary);
            color: var(--text-primary);
            display: flex;
            min-height: 100vh;
            overflow-x: hidden;
            transition: background var(--transition);
        }
        ::-webkit-scrollbar {
            width: 5px;
            height: 5px;
        }
        ::-webkit-scrollbar-track {
            background: var(--bg-secondary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--accent-1);
            border-radius: 10px;
        }

        /* ============================================================
           LOGIN PAGE
           ============================================================ */
        #loginPage {
            position: fixed;
            inset: 0;
            background: var(--bg-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            padding: 20px;
            background-image: radial-gradient(ellipse at 20% 50%, rgba(99, 102, 241, 0.12) 0%, transparent 60%), radial-gradient(ellipse at 80% 50%, rgba(6, 182, 212, 0.08) 0%, transparent 60%);
        }
        #loginPage .login-box {
            background: var(--glass-bg);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 48px 44px;
            max-width: 420px;
            width: 100%;
            box-shadow: var(--shadow-lg), var(--shadow-glow);
            animation: fadeSlideUp 0.6s ease;
            position: relative;
            overflow: hidden;
        }
        #loginPage .login-box::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(99, 102, 241, 0.04), transparent, rgba(6, 182, 212, 0.04), transparent);
            animation: rotateGlow 12s linear infinite;
            pointer-events: none;
        }
        @keyframes rotateGlow {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
        @keyframes fadeSlideUp {
            0% {
                opacity: 0;
                transform: translateY(30px) scale(0.96);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        #loginPage .login-box .brand {
            text-align: center;
            font-size: 30px;
            font-weight: 900;
            color: var(--text-primary);
            margin-bottom: 4px;
            position: relative;
            z-index: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        #loginPage .login-box .brand svg {
            width: 40px;
            height: 40px;
        }
        #loginPage .login-box .sub {
            text-align: center;
            color: var(--text-secondary);
            font-size: 14px;
            margin-bottom: 32px;
            position: relative;
            z-index: 1;
        }
        #loginPage .login-box .form-group {
            margin-bottom: 18px;
            position: relative;
            z-index: 1;
        }
        #loginPage .login-box label {
            display: block;
            font-weight: 600;
            font-size: 13px;
            color: var(--text-secondary);
            margin-bottom: 5px;
        }
        #loginPage .login-box input,
        #loginPage .login-box select {
            width: 100%;
            padding: 12px 16px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: var(--radius-sm);
            font-size: 14px;
            color: var(--text-primary);
            transition: var(--transition);
            font-family: var(--font);
            outline: none;
        }
        #loginPage .login-box input:focus,
        #loginPage .login-box select:focus {
            border-color: var(--accent-1);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.10);
            background: rgba(255, 255, 255, 0.06);
        }
        #loginPage .login-box input::placeholder {
            color: var(--text-muted);
        }
        #loginPage .login-box .btn-login {
            width: 100%;
            padding: 14px;
            background: var(--accent-gradient);
            color: #fff;
            border: none;
            border-radius: var(--radius-sm);
            font-weight: 700;
            font-size: 16px;
            cursor: pointer;
            transition: var(--transition);
            margin-top: 8px;
            position: relative;
            z-index: 1;
            font-family: var(--font);
        }
        #loginPage .login-box .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(99, 102, 241, 0.35);
        }
        #loginPage .login-box .error-msg {
            color: var(--danger);
            font-size: 13px;
            margin-top: 12px;
            text-align: center;
            display: none;
            position: relative;
            z-index: 1;
        }
        .login-options {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 8px;
            font-size: 13px;
            flex-wrap: wrap;
            gap: 6px;
            position: relative;
            z-index: 1;
        }
        .login-options label {
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            color: var(--text-secondary);
        }
        .login-options a {
            color: var(--accent-1);
            text-decoration: none;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
        }
        .login-options a:hover {
            color: var(--accent-2);
            text-decoration: underline;
        }

        /* ============================================================
           APP CONTAINER
           ============================================================ */
        #appContainer {
            display: none;
            width: 100%;
            min-height: 100vh;
        }

        /* ============================================================
           SIDEBAR
           ============================================================ */
        .sidebar {
            width: var(--sidebar-width);
            background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 255, 255, 0.04);
            color: var(--text-secondary);
            display: flex;
            flex-direction: column;
            padding: 24px 16px 20px;
            position: sticky;
            top: 0;
            height: 100vh;
            overflow-y: auto;
            flex-shrink: 0;
            transition: width 0.3s ease, background var(--transition);
            z-index: 100;
        }
        .sidebar .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 22px;
            font-weight: 900;
            padding-bottom: 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            margin-bottom: 24px;
        }
        .sidebar .brand svg {
            width: 36px;
            height: 36px;
        }
        .sidebar .brand span {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .sidebar .role-badge {
            font-size: 11px;
            font-weight: 600;
            background: rgba(99, 102, 241, 0.08);
            padding: 4px 14px;
            border-radius: 30px;
            color: var(--accent-1);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 20px;
            width: fit-content;
            border: 1px solid rgba(99, 102, 241, 0.06);
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .sidebar .nav-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 11px 16px;
            border-radius: 12px;
            cursor: pointer;
            transition: all var(--transition);
            color: var(--text-secondary);
            font-weight: 500;
            font-size: 14px;
            margin-bottom: 2px;
            position: relative;
        }
        .sidebar .nav-item i {
            width: 20px;
            font-size: 16px;
            text-align: center;
            transition: var(--transition);
        }
        .sidebar .nav-item:hover {
            background: rgba(255, 255, 255, 0.04);
            color: var(--text-primary);
        }
        .sidebar .nav-item.active {
            background: rgba(99, 102, 241, 0.08);
            color: var(--text-primary);
        }
        .sidebar .nav-item.active::before {
            content: '';
            position: absolute;
            left: -16px;
            top: 50%;
            transform: translateY(-50%);
            width: 3px;
            height: 28px;
            background: var(--accent-gradient);
            border-radius: 0 4px 4px 0;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
        }
        .sidebar .nav-item.active i {
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .sidebar .nav-item .badge {
            margin-left: auto;
            background: var(--danger);
            color: #fff;
            font-size: 10px;
            font-weight: 700;
            padding: 2px 9px;
            border-radius: 30px;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.15);
        }
        .sidebar .nav-item.signout {
            margin-top: auto;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
            padding-top: 18px;
            color: var(--text-muted);
        }
        .sidebar .nav-item.signout:hover {
            color: var(--danger);
            background: transparent;
        }
        .sidebar .nav-item.admin-only {
            display: flex;
        }
        .sidebar .nav-item.customer-only {
            display: none;
        }
        body.customer-mode .sidebar .nav-item.admin-only {
            display: none;
        }
        body.customer-mode .sidebar .nav-item.customer-only {
            display: flex;
        }

        /* ============================================================
           MAIN CONTENT
           ============================================================ */
        .main {
            flex: 1;
            padding: 28px 40px 40px;
            overflow-y: auto;
            min-height: 100vh;
            background: var(--bg-primary);
        }
        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 32px;
            flex-wrap: wrap;
            gap: 14px;
        }
        .topbar h1 {
            font-size: 28px;
            font-weight: 900;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }
        .topbar h1 span {
            font-weight: 400;
            font-size: 16px;
            color: var(--text-secondary);
            -webkit-text-fill-color: var(--text-secondary);
            margin-left: 8px;
        }
        .topbar-right {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }
        .topbar-right .admin-badge {
            background: rgba(255, 255, 255, 0.03);
            padding: 7px 18px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-primary);
            border: 1px solid rgba(255, 255, 255, 0.04);
            display: flex;
            align-items: center;
            gap: 8px;
            backdrop-filter: blur(10px);
        }
        .topbar-right .admin-badge i {
            color: var(--accent-1);
        }
        .theme-toggle,
        .notif-btn {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.04);
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
            color: var(--text-primary);
            font-size: 18px;
            cursor: pointer;
            backdrop-filter: blur(10px);
            position: relative;
        }
        .theme-toggle:hover,
        .notif-btn:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.08);
        }
        .notif-dot {
            position: absolute;
            top: -2px;
            right: -2px;
            width: 18px;
            height: 18px;
            background: var(--danger);
            color: #fff;
            font-size: 9px;
            font-weight: 700;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 2px solid var(--bg-primary);
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.15);
        }

        /* ============================================================
           PAGES & CARDS
           ============================================================ */
        .page {
            display: none;
            animation: fadeSlide 0.4s ease;
        }
        .page.active {
            display: block;
        }
        @keyframes fadeSlide {
            0% {
                opacity: 0;
                transform: translateY(12px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 32px;
        }
        .stat-card {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius);
            padding: 22px 24px;
            transition: all var(--transition);
            cursor: default;
            position: relative;
            overflow: hidden;
        }
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: var(--accent-gradient);
            opacity: 0;
            transition: var(--transition);
        }
        .stat-card:hover::before {
            opacity: 1;
        }
        .stat-card:hover {
            background: var(--bg-card-hover);
            border-color: rgba(255, 255, 255, 0.08);
            transform: translateY(-4px);
            box-shadow: var(--shadow-md), var(--shadow-glow);
        }
        .stat-card .top-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .stat-card .label {
            font-size: 14px;
            color: var(--text-secondary);
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .stat-card .value {
            font-size: 36px;
            font-weight: 900;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-top: 4px;
            letter-spacing: -0.5px;
        }
        .stat-card .change {
            font-size: 13px;
            font-weight: 600;
            margin-top: 4px;
        }
        .stat-card .change.positive {
            color: var(--success);
        }
        .stat-card .change.negative {
            color: var(--danger);
        }
        .stat-card .icon-circle {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            background: rgba(99, 102, 241, 0.06);
            color: var(--accent-1);
            transition: var(--transition);
        }
        .stat-card:hover .icon-circle {
            background: rgba(99, 102, 241, 0.12);
            transform: scale(1.05);
        }

        .charts-row {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
            margin-bottom: 32px;
        }
        .chart-card {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius);
            padding: 22px 24px 24px;
            transition: var(--transition);
        }
        .chart-card:hover {
            border-color: rgba(255, 255, 255, 0.06);
        }
        .chart-card .chart-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        .chart-card .chart-header h3 {
            font-size: 16px;
            font-weight: 700;
            color: var(--text-primary);
        }
        .chart-card .chart-header .sub {
            font-size: 13px;
            color: var(--text-muted);
        }
        .chart-container {
            position: relative;
            height: 140px;
        }
        .chart-container canvas {
            width: 100% !important;
            height: 100% !important;
        }

        .card {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius);
            padding: 22px 24px 24px;
            margin-bottom: 24px;
            transition: var(--transition);
        }
        .card:hover {
            border-color: rgba(255, 255, 255, 0.05);
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            flex-wrap: wrap;
            gap: 12px;
        }
        .card-header h3 {
            font-size: 17px;
            font-weight: 700;
            color: var(--text-primary);
        }
        .flex-between {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        /* ============================================================
           BUTTONS
           ============================================================ */
        .btn {
            background: var(--accent-gradient);
            color: #ffffff;
            border: none;
            padding: 9px 24px;
            border-radius: var(--radius-sm);
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            transition: all var(--transition);
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font);
            position: relative;
            overflow: hidden;
        }
        .btn::after {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.06), transparent);
            opacity: 0;
            transition: var(--transition);
        }
        .btn:hover::after {
            opacity: 1;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(99, 102, 241, 0.25);
        }
        .btn-outline {
            background: transparent;
            color: var(--text-primary);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        .btn-outline:hover {
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(255, 255, 255, 0.10);
            box-shadow: none;
            transform: none;
        }
        .btn-sm {
            padding: 5px 14px;
            font-size: 12px;
            border-radius: var(--radius-xs);
            gap: 5px;
        }
        .btn-danger {
            background: var(--danger);
        }
        .btn-danger:hover {
            background: #dc2626;
            box-shadow: 0 8px 30px rgba(239, 68, 68, 0.2);
        }
        .btn-success {
            background: var(--success);
        }
        .btn-success:hover {
            background: #059669;
            box-shadow: 0 8px 30px rgba(16, 185, 129, 0.2);
        }
        .btn-warning {
            background: var(--warning);
        }
        .btn-warning:hover {
            background: #d97706;
            box-shadow: 0 8px 30px rgba(245, 158, 11, 0.2);
        }

        /* ============================================================
           TABLES
           ============================================================ */
        .table-wrap {
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }
        table th {
            text-align: left;
            padding: 12px 8px 12px 0;
            color: var(--text-secondary);
            font-weight: 600;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        table td {
            padding: 12px 8px 12px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.02);
            vertical-align: middle;
            color: var(--text-primary);
        }
        table tr:last-child td {
            border-bottom: none;
        }
        table tr:hover td {
            background: rgba(255, 255, 255, 0.01);
        }
        table tr:nth-child(even) td {
            background: rgba(255, 255, 255, 0.005);
        }
        .table-wrap table .checkbox-cell {
            width: 30px;
        }
        .table-wrap table .checkbox-cell input[type="checkbox"] {
            accent-color: var(--accent-1);
            width: 16px;
            height: 16px;
            cursor: pointer;
        }

        /* ============================================================
           STATUS BADGES
           ============================================================ */
        .status-badge {
            padding: 3px 14px;
            border-radius: 30px;
            font-size: 10px;
            font-weight: 700;
            display: inline-block;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .status-badge.active,
        .status-badge.paid,
        .status-badge.online {
            background: rgba(16, 185, 129, 0.10);
            color: var(--success);
            border: 1px solid rgba(16, 185, 129, 0.06);
        }
        .status-badge.pending,
        .status-badge.open {
            background: rgba(245, 158, 11, 0.10);
            color: var(--warning);
            border: 1px solid rgba(245, 158, 11, 0.06);
        }
        .status-badge.inactive,
        .status-badge.unpaid,
        .status-badge.offline {
            background: rgba(239, 68, 68, 0.10);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.06);
        }
        .status-badge.closed {
            background: rgba(255, 255, 255, 0.02);
            color: var(--text-secondary);
            border: 1px solid rgba(255, 255, 255, 0.02);
        }
        .status-badge.high {
            background: rgba(239, 68, 68, 0.10);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.06);
        }
        .status-badge.medium {
            background: rgba(245, 158, 11, 0.10);
            color: var(--warning);
            border: 1px solid rgba(245, 158, 11, 0.06);
        }
        .status-badge.low {
            background: rgba(99, 102, 241, 0.06);
            color: var(--accent-1);
            border: 1px solid rgba(99, 102, 241, 0.04);
        }
        .status-badge.overdue {
            background: rgba(239, 68, 68, 0.15);
            color: var(--danger);
            border: 1px solid rgba(239, 68, 68, 0.12);
            animation: pulseBadge 1.5s ease-in-out infinite;
        }
        @keyframes pulseBadge {
            0%,
            100% {
                opacity: 1;
            }
            50% {
                opacity: 0.6;
            }
        }

        /* ============================================================
           NETWORK TOPOLOGY DIAGRAM
           ============================================================ */
        .topology-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 0;
            gap: 20px;
        }
        .topology-layer {
            display: flex;
            gap: 30px;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
        }
        .topology-node {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 12px 18px;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: var(--radius-sm);
            min-width: 80px;
            transition: var(--transition);
            cursor: default;
        }
        .topology-node:hover {
            background: var(--bg-card-hover);
            transform: translateY(-2px);
            border-color: rgba(255, 255, 255, 0.10);
        }
        .topology-node .icon {
            font-size: 28px;
            margin-bottom: 4px;
        }
        .topology-node .icon.router {
            color: var(--accent-1);
        }
        .topology-node .icon.switch {
            color: var(--accent-3);
        }
        .topology-node .icon.ap {
            color: var(--success);
        }
        .topology-node .label {
            font-size: 11px;
            font-weight: 600;
            color: var(--text-secondary);
        }
        .topology-node .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
            margin-top: 2px;
        }
        .topology-node .status-dot.online {
            background: var(--success);
        }
        .topology-node .status-dot.offline {
            background: var(--danger);
        }

        /* ============================================================
           OUTAGE DASHBOARD
           ============================================================ */
        .outage-item {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.02);
        }
        .outage-item:last-child {
            border-bottom: none;
        }
        .outage-item .severity {
            width: 6px;
            height: 40px;
            border-radius: 4px;
            flex-shrink: 0;
        }
        .outage-item .severity.critical {
            background: var(--danger);
        }
        .outage-item .severity.major {
            background: var(--warning);
        }
        .outage-item .severity.minor {
            background: var(--accent-1);
        }
        .outage-item .outage-info {
            flex: 1;
        }
        .outage-item .outage-info .title {
            font-weight: 600;
            color: var(--text-primary);
            font-size: 14px;
        }
        .outage-item .outage-info .desc {
            font-size: 13px;
            color: var(--text-secondary);
        }
        .outage-item .outage-time {
            font-size: 12px;
            color: var(--text-muted);
            text-align: right;
        }

        /* ============================================================
           IP POOL
           ============================================================ */
        .ip-pool-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
            gap: 10px;
            margin-top: 12px;
        }
        .ip-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 10px 8px;
            border-radius: var(--radius-xs);
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            transition: var(--transition);
            font-size: 13px;
        }
        .ip-item:hover {
            background: var(--bg-card-hover);
        }
        .ip-item .ip-address {
            font-weight: 600;
            color: var(--text-primary);
            font-size: 13px;
        }
        .ip-item .ip-status {
            font-size: 10px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }
        .ip-item .ip-status.available {
            color: var(--success);
        }
        .ip-item .ip-status.assigned {
            color: var(--warning);
        }
        .ip-item .ip-status.reserved {
            color: var(--accent-1);
        }

        /* ============================================================
           SEARCH & FILTERS
           ============================================================ */
        .search-bar {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 30px;
            padding: 5px 18px 5px 20px;
            border: 1px solid rgba(255, 255, 255, 0.03);
            transition: var(--transition);
            min-width: 200px;
        }
        .search-bar:focus-within {
            border-color: rgba(99, 102, 241, 0.12);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.02);
        }
        .search-bar input {
            border: none;
            background: transparent;
            padding: 8px 0;
            font-size: 14px;
            outline: none;
            flex: 1;
            color: var(--text-primary);
            font-family: var(--font);
        }
        .search-bar input::placeholder {
            color: var(--text-muted);
        }
        .search-bar i {
            color: var(--text-muted);
            font-size: 15px;
        }
        .filter-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
        }
        .filter-group select {
            padding: 8px 14px;
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: var(--radius-xs);
            background: rgba(255, 255, 255, 0.02);
            color: var(--text-primary);
            font-size: 13px;
            font-family: var(--font);
            cursor: pointer;
            transition: var(--transition);
            outline: none;
        }
        .filter-group select:focus {
            border-color: rgba(99, 102, 241, 0.12);
        }

        /* ============================================================
           PACKAGE CARDS
           ============================================================ */
        .pkg-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
            gap: 18px;
        }
        .pkg-card {
            background: var(--glass-bg);
            border-radius: 14px;
            padding: 24px 18px;
            border: 1px solid var(--glass-border);
            text-align: center;
            transition: all var(--transition);
            backdrop-filter: blur(12px);
        }
        .pkg-card:hover {
            border-color: rgba(255, 255, 255, 0.08);
            transform: translateY(-4px);
            box-shadow: var(--shadow-md), var(--shadow-glow);
        }
        .pkg-card .pkg-name {
            font-weight: 800;
            font-size: 18px;
            color: var(--text-primary);
        }
        .pkg-card .pkg-speed {
            font-size: 14px;
            color: var(--text-secondary);
            margin: 4px 0 8px;
        }
        .pkg-card .pkg-price {
            font-size: 26px;
            font-weight: 900;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .pkg-card .pkg-price small {
            font-weight: 400;
            font-size: 14px;
            color: var(--text-secondary);
            -webkit-text-fill-color: var(--text-secondary);
        }
        .pkg-card .btn {
            margin-top: 12px;
            width: 100%;
            justify-content: center;
        }

        /* ============================================================
           PAGINATION
           ============================================================ */
        .pagination {
            display: flex;
            gap: 6px;
            justify-content: flex-end;
            margin-top: 14px;
        }
        .pagination .page-btn {
            padding: 4px 12px;
            border-radius: var(--radius-xs);
            border: 1px solid rgba(255, 255, 255, 0.03);
            background: rgba(255, 255, 255, 0.01);
            color: var(--text-secondary);
            font-size: 13px;
            cursor: pointer;
            transition: var(--transition);
        }
        .pagination .page-btn:hover {
            background: rgba(255, 255, 255, 0.03);
            border-color: rgba(255, 255, 255, 0.06);
        }
        .pagination .page-btn.active {
            background: var(--accent-gradient);
            color: #fff;
            border-color: transparent;
        }
        .pagination .page-btn.disabled {
            opacity: 0.3;
            pointer-events: none;
        }

        /* ============================================================
           MODAL
           ============================================================ */
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 999;
            padding: 20px;
        }
        .modal-overlay.open {
            display: flex;
        }
        .modal-box {
            background: rgba(0, 0, 0, 0.94);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 32px 36px;
            max-width: 540px;
            width: 100%;
            max-height: 92vh;
            overflow-y: auto;
            box-shadow: var(--shadow-lg), var(--shadow-glow);
            animation: fadeSlide 0.25s ease;
        }
        .modal-box h2 {
            font-size: 22px;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 4px;
        }
        .modal-box .sub {
            color: var(--text-secondary);
            margin-bottom: 22px;
            font-size: 14px;
        }
        .modal-box .form-group {
            margin-bottom: 16px;
        }
        .modal-box label {
            display: block;
            font-weight: 600;
            font-size: 13px;
            margin-bottom: 5px;
            color: var(--text-secondary);
        }
        .modal-box input,
        .modal-box select,
        .modal-box textarea {
            width: 100%;
            padding: 10px 14px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: var(--radius-sm);
            font-size: 14px;
            color: var(--text-primary);
            transition: var(--transition);
            font-family: var(--font);
            outline: none;
        }
        .modal-box input:focus,
        .modal-box select:focus,
        .modal-box textarea:focus {
            border-color: rgba(99, 102, 241, 0.15);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.02);
        }
        .modal-box .field-hint {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 3px;
        }
        .modal-actions {
            display: flex;
            gap: 12px;
            margin-top: 24px;
            justify-content: flex-end;
        }
        .modal-actions .btn {
            padding: 10px 28px;
        }

        /* ============================================================
           TOAST
           ============================================================ */
        #toastContainer {
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 360px;
            width: 100%;
        }
        .toast {
            background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            color: var(--text-primary);
            padding: 14px 20px;
            border-radius: var(--radius-sm);
            box-shadow: var(--shadow-lg);
            display: flex;
            align-items: center;
            gap: 12px;
            animation: slideUp 0.4s ease;
            font-size: 14px;
            font-weight: 500;
            border-left: 4px solid var(--accent-1);
        }
        .toast.success {
            border-left-color: var(--success);
        }
        .toast.error {
            border-left-color: var(--danger);
        }
        .toast.warning {
            border-left-color: var(--warning);
        }
        .toast i {
            font-size: 18px;
        }
        .toast .toast-close {
            margin-left: auto;
            cursor: pointer;
            opacity: 0.6;
            transition: var(--transition);
        }
        .toast .toast-close:hover {
            opacity: 1;
        }
        @keyframes slideUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .text-muted {
            color: var(--text-muted);
        }

        /* ============================================================
           BULK ACTIONS BAR
           ============================================================ */
        .bulk-actions-bar {
            display: none;
            align-items: center;
            justify-content: space-between;
            background: rgba(99, 102, 241, 0.08);
            border: 1px solid rgba(99, 102, 241, 0.15);
            padding: 10px 20px;
            border-radius: var(--radius-sm);
            margin-bottom: 16px;
            animation: fadeSlide 0.3s ease;
        }
        .bulk-actions-bar.visible {
            display: flex;
        }
        .bulk-actions-bar .count {
            font-weight: 600;
            color: var(--accent-1);
        }
        .bulk-actions-bar .actions {
            display: flex;
            gap: 10px;
        }

        /* ============================================================
           FAQ / HELP CENTER
           ============================================================ */
        .faq-item {
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            padding: 16px 0;
        }
        .faq-item:last-child {
            border-bottom: none;
        }
        .faq-item .question {
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            font-weight: 600;
            font-size: 15px;
            color: var(--text-primary);
            transition: var(--transition);
            padding: 4px 0;
        }
        .faq-item .question:hover {
            color: var(--accent-1);
        }
        .faq-item .question i {
            font-size: 12px;
            transition: transform 0.3s ease;
            color: var(--text-muted);
        }
        .faq-item.open .question i {
            transform: rotate(180deg);
        }
        .faq-item .answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease, padding 0.3s ease;
            color: var(--text-secondary);
            font-size: 14px;
            line-height: 1.7;
            padding: 0 0 0 16px;
            border-left: 2px solid var(--accent-1);
            margin-top: 0;
        }
        .faq-item.open .answer {
            max-height: 200px;
            margin-top: 10px;
            padding: 10px 0 10px 16px;
        }

        /* ============================================================
           FORMS INSIDE CARDS
           ============================================================ */
        .card .form-group {
            margin-bottom: 18px;
        }
        .card .form-group label {
            display: block;
            font-weight: 600;
            font-size: 13px;
            color: var(--text-secondary);
            margin-bottom: 6px;
        }
        .card .form-group input,
        .card .form-group select,
        .card .form-group textarea {
            width: 100%;
            padding: 11px 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: var(--radius-sm);
            font-size: 14px;
            color: var(--text-primary);
            transition: var(--transition);
            font-family: var(--font);
            outline: none;
        }
        .card .form-group input:focus,
        .card .form-group select:focus,
        .card .form-group textarea:focus {
            border-color: var(--accent-1);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.06);
            background: rgba(255, 255, 255, 0.04);
        }
        .card .form-group input::placeholder {
            color: var(--text-muted);
        }
        .card .form-group select {
            cursor: pointer;
            appearance: none;
            -webkit-appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 14px center;
            padding-right: 36px;
        }
        .card .form-group select option {
            background: var(--bg-secondary);
            color: var(--text-primary);
        }

        /* ============================================================
           RESPONSIVE
           ============================================================ */
        @media (max-width: 1024px) {
            .charts-row {
                grid-template-columns: 1fr;
            }
            .topology-layer {
                gap: 16px;
            }
            .topology-node {
                min-width: 60px;
                padding: 8px 12px;
            }
            .topology-node .icon {
                font-size: 20px;
            }
        }
        @media (max-width: 820px) {
            .sidebar {
                width: 72px;
                padding: 16px 10px;
            }
            .sidebar .brand span,
            .sidebar .nav-item span,
            .sidebar .role-badge span {
                display: none;
            }
            .sidebar .brand {
                justify-content: center;
                padding-bottom: 16px;
                margin-bottom: 16px;
            }
            .sidebar .brand svg {
                width: 32px;
                height: 32px;
            }
            .sidebar .nav-item {
                justify-content: center;
                padding: 12px;
            }
            .sidebar .nav-item i {
                font-size: 18px;
                margin: 0;
            }
            .sidebar .nav-item .badge {
                display: none;
            }
            .sidebar .role-badge {
                justify-content: center;
                padding: 4px 10px;
                font-size: 10px;
                margin: 0 auto 14px;
            }
            .sidebar .nav-item.active::before {
                left: -10px;
                height: 20px;
            }
            .main {
                padding: 18px 14px 30px;
            }
            .topbar h1 {
                font-size: 20px;
            }
            .topbar h1 span {
                display: none;
            }
            .stats-grid {
                grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
                gap: 12px;
            }
            .stat-card .value {
                font-size: 26px;
            }
            .modal-box {
                padding: 24px 20px;
            }
            .pkg-grid {
                grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            }
            .ip-pool-grid {
                grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
            }
            .outage-item {
                flex-wrap: wrap;
            }
            .outage-item .outage-time {
                text-align: left;
                width: 100%;
            }
        }
        @media (max-width: 480px) {
            .stats-grid {
                grid-template-columns: 1fr 1fr;
            }
            .topbar-right .admin-badge span {
                display: none;
            }
            .flex-between {
                flex-direction: column;
                align-items: stretch;
            }
            .search-bar {
                max-width: 100%;
            }
            .filter-group {
                flex-direction: column;
                align-items: stretch;
            }
            .modal-actions {
                flex-direction: column;
            }
            .modal-actions .btn {
                width: 100%;
                justify-content: center;
            }
            #toastContainer {
                right: 16px;
                left: 16px;
                max-width: 100%;
            }
            #loginPage .login-box {
                padding: 32px 24px;
            }
            .ip-pool-grid {
                grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
            }
            .topology-layer {
                flex-direction: column;
                gap: 8px;
            }
        }
    </style>
</head>
<body>
    <!-- ==================== LOGIN PAGE ==================== -->
    <div id="loginPage">
        <div class="login-box">
            <div class="brand">
                <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                    <rect width="512" height="512" rx="72" fill="url(#brandGrad)"/>
                    <text x="256" y="320" font-size="240" font-family="Arial" text-anchor="middle" fill="white">N</text>
                    <defs>
                        <linearGradient id="brandGrad" gradientTransform="rotate(45)">
                            <stop offset="0%" stop-color="#6366f1"/>
                            <stop offset="50%" stop-color="#8b5cf6"/>
                            <stop offset="100%" stop-color="#06b6d4"/>
                        </linearGradient>
                    </defs>
                </svg>
                NetSphere
            </div>
            <div class="sub">Enterprise ISP Management</div>
            <div class="form-group">
                <label>Role</label>
                <select id="loginRole">
                    <option value="admin">Admin</option>
                    <option value="customer">Customer</option>
                </select>
            </div>
            <div class="form-group">
                <label>Username</label>
                <input type="text" id="loginUser" value="admin" placeholder="Enter username" required />
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" id="loginPass" value="admin" placeholder="Enter password" required />
            </div>
            <div class="login-options">
                <label><input type="checkbox" id="rememberMe" /> Remember me</label>
                <a id="registerLink" style="cursor:pointer; color:var(--accent-1);">Register</a>
                <a href="#" id="forgotPassword">Forgot password?</a>
            </div>
            <button class="btn-login" id="loginBtn"><i class="fas fa-sign-in-alt"></i> Sign In</button>
            <div class="error-msg" id="loginError">Invalid credentials. Please try again.</div>
        </div>
    </div>

    <!-- ==================== APP CONTAINER ==================== -->
    <div id="appContainer">
        <!-- ==================== SIDEBAR ==================== -->
        <aside class="sidebar" id="sidebar">
            <div class="brand">
                <svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" width="36" height="36">
                    <rect width="512" height="512" rx="72" fill="url(#brandGrad2)"/>
                    <text x="256" y="320" font-size="240" font-family="Arial" text-anchor="middle" fill="white">N</text>
                    <defs>
                        <linearGradient id="brandGrad2" gradientTransform="rotate(45)">
                            <stop offset="0%" stop-color="#6366f1"/>
                            <stop offset="50%" stop-color="#8b5cf6"/>
                            <stop offset="100%" stop-color="#06b6d4"/>
                        </linearGradient>
                    </defs>
                </svg>
                <span>NetSphere</span>
            </div>
            <div class="role-badge" id="sidebarRoleBadge"><i class="fas fa-user-shield"></i> <span id="roleLabel">Admin</span></div>

            <!-- Admin Items -->
            <div class="nav-item active admin-only" data-page="dashboard"><i class="fas fa-th-large"></i><span>Dashboard</span></div>
            <div class="nav-item admin-only" data-page="customers"><i class="fas fa-users"></i><span>Customers</span><span class="badge" id="customerBadge">0</span></div>
            <div class="nav-item admin-only" data-page="packages"><i class="fas fa-box"></i><span>Packages</span></div>
            <div class="nav-item admin-only" data-page="billing"><i class="fas fa-file-invoice-dollar"></i><span>Billing</span><span class="badge" id="billingBadge">0</span></div>
            <div class="nav-item admin-only" data-page="tickets"><i class="fas fa-ticket-alt"></i><span>Tickets</span><span class="badge" id="ticketBadge">0</span></div>
            <div class="nav-item admin-only" data-page="staff"><i class="fas fa-user-tie"></i><span>Staff</span></div>
            <div class="nav-item admin-only" data-page="network-ops"><i class="fas fa-network-wired"></i><span>Network Ops</span></div>
            <div class="nav-item admin-only" data-page="reports"><i class="fas fa-chart-bar"></i><span>Reports</span></div>
            <div class="nav-item admin-only" data-page="map"><i class="fas fa-map-marked-alt"></i><span>Map</span></div>
            <div class="nav-item admin-only" data-page="help"><i class="fas fa-life-ring"></i><span>Help Center</span></div>
            <div class="nav-item admin-only" data-page="activity"><i class="fas fa-history"></i><span>Activity Logs</span></div>

            <!-- Customer Items -->
            <div class="nav-item customer-only active" data-page="c-dashboard"><i class="fas fa-home"></i><span>My Dashboard</span></div>
            <div class="nav-item customer-only" data-page="c-profile"><i class="fas fa-user"></i><span>My Profile</span></div>
            <div class="nav-item customer-only" data-page="c-payments"><i class="fas fa-credit-card"></i><span>My Payments</span></div>
            <div class="nav-item customer-only" data-page="c-tickets"><i class="fas fa-ticket-alt"></i><span>My Tickets</span></div>
            <div class="nav-item customer-only" data-page="c-submit"><i class="fas fa-plus-circle"></i><span>Submit Ticket</span></div>

            <div class="nav-item signout" id="signOutBtn"><i class="fas fa-sign-out-alt"></i><span>Sign Out</span></div>
        </aside>

        <!-- ==================== MAIN CONTENT ==================== -->
        <main class="main" id="mainContent">
            <header class="topbar">
                <h1 id="pageTitle">Dashboard <span>– overview</span></h1>
                <div class="topbar-right">
                    <div class="admin-badge" id="headerBadge"><i class="fas fa-crown"></i> <span id="headerRole">Admin</span></div>
                    <button class="theme-toggle" id="themeToggle"><i class="fas fa-moon"></i></button>
                    <button class="notif-btn" id="notifToggle">
                        <i class="fas fa-bell"></i>
                        <span class="notif-dot" id="notifDot">3</span>
                    </button>
                </div>
            </header>

            <!-- ============================================================ -->
            <!-- ADMIN PAGES -->
            <!-- ============================================================ -->

            <!-- DASHBOARD -->
            <section class="page active" id="page-dashboard">
                <div class="stats-grid">
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-users"></i> Total Customers</span><span class="icon-circle"><i class="fas fa-user"></i></span></div><div class="value" id="statCustomers">0</div><div class="change positive"><i class="fas fa-arrow-up"></i> 12% this month</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-wifi"></i> Active Connections</span><span class="icon-circle"><i class="fas fa-signal"></i></span></div><div class="value" id="statConnections">0</div><div class="change positive"><i class="fas fa-arrow-up"></i> 8% this month</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-ticket-alt"></i> Open Tickets</span><span class="icon-circle"><i class="fas fa-ticket"></i></span></div><div class="value" id="statTickets">0</div><div class="change negative"><i class="fas fa-arrow-down"></i> 3% this month</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-dollar-sign"></i> Total Revenue</span><span class="icon-circle"><i class="fas fa-coins"></i></span></div><div class="value" id="statRevenue">$0</div><div class="change positive"><i class="fas fa-arrow-up"></i> 18% this month</div></div>
                </div>
                <div class="charts-row">
                    <div class="chart-card"><div class="chart-header"><h3>Revenue Trend</h3><span class="sub">Last 6 months</span></div><div class="chart-container"><canvas id="revenueChart"></canvas></div></div>
                    <div class="chart-card"><div class="chart-header"><h3>Package Distribution</h3><span class="sub">Active subscribers</span></div><div class="chart-container"><canvas id="packageChart"></canvas></div></div>
                </div>
                <div style="display:grid; grid-template-columns: 2fr 1fr; gap:20px;">
                    <div class="card"><div class="card-header"><h3>Recent Payments</h3></div><div class="table-wrap"><table><thead><tr><th>Receipt</th><th>Customer</th><th>Amount</th><th>Status</th></tr></thead><tbody id="recentPayments"></tbody></table></div></div>
                    <div class="card"><div class="card-header"><h3>System Snapshot</h3></div><div style="font-size:15px; line-height:2.4;"><div><span class="text-muted">Active Packages</span> <strong id="snapPackages">0</strong></div><div><span class="text-muted">Pending Invoices</span> <strong id="snapPending">0</strong></div><div><span class="text-muted">Open Tickets</span> <strong id="snapOpenTickets">0</strong></div><div><span class="text-muted">Staff Members</span> <strong id="snapStaff">0</strong></div><div><span class="text-muted">Total Revenue</span> <strong id="snapRevenueYTD">$0</strong></div><div><span class="text-muted">System Status</span> <strong id="systemStatus" style="color:var(--success);">● Operational</strong></div></div></div>
                </div>
            </section>

            <!-- CUSTOMERS -->
            <section class="page" id="page-customers">
                <div class="flex-between" style="margin-bottom:18px;">
                    <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
                        <div class="search-bar"><i class="fas fa-search"></i><input type="text" id="customerSearch" placeholder="Search by name or email..." /></div>
                        <div class="filter-group">
                            <select id="filterPackage"><option value="">All Packages</option><option value="Fiber 50">Fiber 50</option><option value="Fiber 100">Fiber 100</option><option value="Fiber 200">Fiber 200</option><option value="Fiber 500">Fiber 500</option></select>
                            <select id="filterStatus"><option value="">All Status</option><option value="active">Active</option><option value="inactive">Inactive</option></select>
                        </div>
                    </div>
                    <div style="display:flex; gap:8px;">
                        <button class="btn btn-outline btn-sm" id="exportCsvBtn"><i class="fas fa-file-csv"></i> Export CSV</button>
                        <button class="btn btn-outline btn-sm" id="bulkImportBtn"><i class="fas fa-upload"></i> Bulk Import</button>
                        <button class="btn" id="btnAddCustomer"><i class="fas fa-plus"></i> Add Customer</button>
                    </div>
                </div>

                <!-- Bulk Actions Bar -->
                <div class="bulk-actions-bar" id="bulkActionsBar">
                    <span class="count" id="bulkCount">0 selected</span>
                    <div class="actions">
                        <button class="btn btn-sm btn-danger" id="bulkDeleteBtn"><i class="fas fa-trash"></i> Delete Selected</button>
                        <button class="btn btn-sm btn-outline" id="bulkClearBtn"><i class="fas fa-times"></i> Clear</button>
                    </div>
                </div>

                <div class="card">
                    <div class="table-wrap">
                        <table>
                            <thead><tr><th class="checkbox-cell"><input type="checkbox" id="selectAllCustomers" /></th><th>Customer</th><th>Email</th><th>Package</th><th>Data Used</th><th>Status</th><th>Connection</th><th>Actions</th></tr></thead>
                            <tbody id="customerTableBody"></tbody>
                        </table>
                    </div>
                    <div class="pagination" id="customerPagination"></div>
                </div>
            </section>

            <!-- PACKAGES -->
            <section class="page" id="page-packages">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Internet Packages</h3><button class="btn" id="btnAddPackage"><i class="fas fa-plus"></i> Create Package</button></div>
                <div class="pkg-grid" id="packageGrid"></div>
            </section>

            <!-- BILLING -->
            <section class="page" id="page-billing">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Billing & Invoices</h3><button class="btn" id="btnAddInvoice"><i class="fas fa-plus"></i> New Invoice</button></div>
                <div class="card"><div class="table-wrap"><table><thead><tr><th>Invoice #</th><th>Customer</th><th>Amount</th><th>Due Date</th><th>Status</th><th>Actions</th></tr></thead><tbody id="billingTableBody"></tbody></table></div></div>
            </section>

            <!-- TICKETS -->
            <section class="page" id="page-tickets">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Support Tickets</h3><button class="btn" id="btnAddTicket"><i class="fas fa-plus"></i> New Ticket</button></div>
                <div class="card"><div class="table-wrap"><table><thead><tr><th>Ticket ID</th><th>Customer</th><th>Subject</th><th>Status</th><th>Priority</th><th>Actions</th></tr></thead><tbody id="ticketTableBody"></tbody></table></div></div>
            </section>

            <!-- STAFF -->
            <section class="page" id="page-staff">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Staff Management</h3><button class="btn" id="btnAddStaff"><i class="fas fa-plus"></i> Add Staff</button></div>
                <div class="card"><div class="table-wrap"><table><thead><tr><th>Name</th><th>Email</th><th>Role</th><th>Status</th><th>Actions</th></tr></thead><tbody id="staffTableBody"></tbody></table></div></div>
            </section>

            <!-- NETWORK OPS -->
            <section class="page" id="page-network-ops">
                <div class="flex-between" style="margin-bottom:18px;">
                    <h3 style="font-weight:700;">Network Operations</h3>
                    <span style="font-size:13px; color:var(--text-muted);"><i class="fas fa-check-circle" style="color:var(--success);"></i> System Online</span>
                </div>
                <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-server"></i> Devices</span><span class="icon-circle"><i class="fas fa-network-wired"></i></span></div><div class="value" id="netDevices">0</div><div class="change positive">All active</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-ip"></i> IP Pool</span><span class="icon-circle"><i class="fas fa-address-book"></i></span></div><div class="value" id="netIPUsage">0%</div><div class="change positive">Used</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-exclamation-triangle"></i> Outages</span><span class="icon-circle"><i class="fas fa-bell"></i></span></div><div class="value" id="netOutages">0</div><div class="change negative" id="netOutageStatus">No outages</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-signal"></i> Avg. Bandwidth</span><span class="icon-circle"><i class="fas fa-chart-line"></i></span></div><div class="value" id="netBandwidth">0 Mbps</div><div class="change positive">Stable</div></div>
                </div>
                <div style="display:flex; gap:4px; margin-bottom:20px; background:var(--glass-bg); border-radius:var(--radius-sm); padding:4px; border:1px solid var(--glass-border); flex-wrap:wrap;">
                    <button class="btn btn-sm btn-outline active" data-net-tab="topology"><i class="fas fa-sitemap"></i> Topology</button>
                    <button class="btn btn-sm btn-outline" data-net-tab="ip-pool"><i class="fas fa-address-book"></i> IP Pool</button>
                    <button class="btn btn-sm btn-outline" data-net-tab="routers"><i class="fas fa-server"></i> Routers/ONU</button>
                    <button class="btn btn-sm btn-outline" data-net-tab="bandwidth"><i class="fas fa-chart-area"></i> Bandwidth</button>
                    <button class="btn btn-sm btn-outline" data-net-tab="outages"><i class="fas fa-exclamation-triangle"></i> Outages</button>
                </div>

                <div class="net-tab-content" id="net-tab-topology">
                    <div class="card"><div class="card-header"><h3>Network Topology</h3><span class="text-muted" style="font-size:13px;"><i class="fas fa-circle" style="color:var(--success);"></i> Online  <i class="fas fa-circle" style="color:var(--danger);margin-left:10px;"></i> Offline</span></div>
                        <div class="topology-container">
                            <div class="topology-layer"><div class="topology-node"><div class="icon router"><i class="fas fa-router"></i></div><div class="label">Core Router</div><span class="status-dot online"></span></div></div>
                            <div style="display:flex; gap:40px; flex-wrap:wrap; justify-content:center;">
                                <div style="display:flex; flex-direction:column; align-items:center; gap:12px;">
                                    <div class="topology-node"><div class="icon switch"><i class="fas fa-arrows-left-right"></i></div><div class="label">Switch A</div><span class="status-dot online"></span></div>
                                    <div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
                                        <div class="topology-node" style="min-width:60px;"><div class="icon ap"><i class="fas fa-wifi"></i></div><div class="label">AP-1</div><span class="status-dot online"></span></div>
                                        <div class="topology-node" style="min-width:60px;"><div class="icon ap"><i class="fas fa-wifi"></i></div><div class="label">AP-2</div><span class="status-dot online"></span></div>
                                        <div class="topology-node" style="min-width:60px;"><div class="icon ap"><i class="fas fa-wifi"></i></div><div class="label">AP-3</div><span class="status-dot offline"></span></div>
                                    </div>
                                </div>
                                <div style="display:flex; flex-direction:column; align-items:center; gap:12px;">
                                    <div class="topology-node"><div class="icon switch"><i class="fas fa-arrows-left-right"></i></div><div class="label">Switch B</div><span class="status-dot online"></span></div>
                                    <div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
                                        <div class="topology-node" style="min-width:60px;"><div class="icon ap"><i class="fas fa-wifi"></i></div><div class="label">AP-4</div><span class="status-dot online"></span></div>
                                        <div class="topology-node" style="min-width:60px;"><div class="icon ap"><i class="fas fa-wifi"></i></div><div class="label">AP-5</div><span class="status-dot online"></span></div>
                                    </div>
                                </div>
                            </div>
                            <div style="font-size:12px; color:var(--text-muted); margin-top:8px;"><i class="fas fa-info-circle"></i> 5/6 devices online · Last updated: <span id="topologyLastUpdate">Just now</span></div>
                        </div>
                    </div>
                </div>

                <div class="net-tab-content" id="net-tab-ip-pool" style="display:none;">
                    <div class="card"><div class="card-header"><h3>IP Address Pool Management</h3><button class="btn btn-sm btn-outline" id="refreshIPPoolBtn"><i class="fas fa-sync"></i> Refresh</button></div>
                        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px; margin-bottom:16px;">
                            <div style="background:var(--glass-bg); border-radius:var(--radius-xs); padding:12px; text-align:center;"><div style="font-size:12px; color:var(--text-muted);">Total IPs</div><div style="font-size:24px; font-weight:800; color:var(--text-primary);" id="ipTotal">256</div></div>
                            <div style="background:var(--glass-bg); border-radius:var(--radius-xs); padding:12px; text-align:center;"><div style="font-size:12px; color:var(--text-muted);">Available</div><div style="font-size:24px; font-weight:800; color:var(--success);" id="ipAvailable">198</div></div>
                            <div style="background:var(--glass-bg); border-radius:var(--radius-xs); padding:12px; text-align:center;"><div style="font-size:12px; color:var(--text-muted);">Assigned</div><div style="font-size:24px; font-weight:800; color:var(--warning);" id="ipAssigned">58</div></div>
                        </div>
                        <div class="ip-pool-grid" id="ipPoolGrid"></div>
                    </div>
                </div>

                <div class="net-tab-content" id="net-tab-routers" style="display:none;">
                    <div class="card"><div class="card-header"><h3>Router / ONU Status</h3><button class="btn btn-sm btn-outline" id="refreshRoutersBtn"><i class="fas fa-sync"></i> Refresh</button></div>
                        <div class="table-wrap"><table><thead><tr><th>Device</th><th>Type</th><th>MAC Address</th><th>Firmware</th><th>Uptime</th><th>Status</th></tr></thead><tbody id="routerTableBody"></tbody></table></div>
                    </div>
                </div>

                <div class="net-tab-content" id="net-tab-bandwidth" style="display:none;">
                    <div class="card"><div class="card-header"><h3>Bandwidth Usage</h3><span class="sub">Monthly cap: 500 GB</span></div>
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px; margin-bottom:16px;">
                            <div><div style="font-size:13px; color:var(--text-muted);">Total Bandwidth Used</div><div style="font-size:28px; font-weight:800; color:var(--text-primary);" id="bandwidthTotal">0 GB</div><div style="font-size:13px; color:var(--text-secondary);" id="bandwidthPercent">0% of cap</div></div>
                            <div><div style="font-size:13px; color:var(--text-muted);">Monthly Cap</div><div style="font-size:28px; font-weight:800; color:var(--text-primary);">500 GB</div><div style="font-size:13px; color:var(--text-secondary);"><span id="bandwidthRemaining">500 GB</span> remaining</div></div>
                        </div>
                        <div style="height:8px; background:var(--glass-bg); border-radius:4px; overflow:hidden; margin-bottom:16px;"><div id="bandwidthBar" style="height:100%; width:0%; background:var(--accent-gradient); border-radius:4px; transition:width 0.8s ease;"></div></div>
                        <div class="chart-container" style="height:160px;"><canvas id="bandwidthUsageChart"></canvas></div>
                        <div style="margin-top:12px; display:flex; gap:12px; flex-wrap:wrap;"><span style="font-size:12px; color:var(--text-muted);"><span style="color:var(--success);">●</span> Daily Usage</span><span style="font-size:12px; color:var(--text-muted);"><span style="color:var(--warning);">●</span> Warning at 80%</span><span style="font-size:12px; color:var(--text-muted);"><span style="color:var(--danger);">●</span> Cap at 100%</span></div>
                    </div>
                </div>

                <div class="net-tab-content" id="net-tab-outages" style="display:none;">
                    <div class="card"><div class="card-header"><h3>Service Outage Dashboard</h3><span class="sub" id="outageSummary">No active outages</span></div>
                        <div id="outageList">
                            <div class="outage-item"><div class="severity critical"></div><div class="outage-info"><div class="title">Core Router Down</div><div class="desc">Affects 12 customers in Zone A</div></div><div class="outage-time">Started: 2 hours ago<br/><span style="color:var(--danger);">CRITICAL</span></div></div>
                            <div class="outage-item"><div class="severity major"></div><div class="outage-info"><div class="title">Switch B Intermittent</div><div class="desc">Affects 5 customers, packet loss 15%</div></div><div class="outage-time">Started: 45 min ago<br/><span style="color:var(--warning);">MAJOR</span></div></div>
                            <div class="outage-item"><div class="severity minor"></div><div class="outage-info"><div class="title">AP-3 Offline</div><div class="desc">Single access point down in Zone C</div></div><div class="outage-time">Started: 10 min ago<br/><span style="color:var(--accent-1);">MINOR</span></div></div>
                            <div class="outage-item" style="border-bottom:none;"><div class="severity" style="background:var(--success);"></div><div class="outage-info"><div class="title">✓ All other services operational</div><div class="desc">No other issues reported</div></div><div class="outage-time" style="color:var(--success);">RESOLVED</div></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- REPORTS -->
            <section class="page" id="page-reports">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Analytics & Reports</h3><button class="btn btn-outline btn-sm" id="exportReportPdf"><i class="fas fa-file-pdf"></i> Export PDF Report</button></div>
                <div class="stats-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-dollar-sign"></i> Total Revenue</span><span class="icon-circle"><i class="fas fa-coins"></i></span></div><div class="value" id="reportTotalRevenue">$0</div><div class="change positive">+18% from last month</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-users"></i> Customer Growth</span><span class="icon-circle"><i class="fas fa-user-plus"></i></span></div><div class="value" id="reportCustomerGrowth">0</div><div class="change positive">+12% from last month</div></div>
                </div>
                <div class="charts-row">
                    <div class="chart-card"><div class="chart-header"><h3>Revenue Over Time</h3><span class="sub">Monthly</span></div><div class="chart-container"><canvas id="revenueReportChart"></canvas></div></div>
                    <div class="chart-card"><div class="chart-header"><h3>Customer Growth</h3><span class="sub">Monthly</span></div><div class="chart-container"><canvas id="growthReportChart"></canvas></div></div>
                </div>
            </section>

            <!-- MAP -->
            <section class="page" id="page-map">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Customer Locations</h3><span class="text-muted" style="font-size:13px;"><i class="fas fa-map-pin"></i> Live customer positions</span></div>
                <div class="card"><div id="customerMap" style="height:350px; border-radius:var(--radius-sm); overflow:hidden; border:1px solid var(--glass-border);"></div></div>
            </section>

            <!-- HELP CENTER -->
            <section class="page" id="page-help">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Help Center</h3><div class="search-bar" style="min-width:180px;"><i class="fas fa-search"></i><input type="text" id="helpSearch" placeholder="Search FAQs..." /></div></div>
                <div class="card" id="faqContainer">
                    <div class="faq-item"><div class="question">How to add a new customer? <i class="fas fa-chevron-down"></i></div><div class="answer">Go to Customers → Click "Add Customer" → Fill in the details → Save.</div></div>
                    <div class="faq-item"><div class="question">How to monitor network devices? <i class="fas fa-chevron-down"></i></div><div class="answer">Go to Network Ops → View Topology, Routers/ONU status, and IP Pool management.</div></div>
                    <div class="faq-item"><div class="question">What does the outage dashboard show? <i class="fas fa-chevron-down"></i></div><div class="answer">It shows real-time service outages with severity levels (Critical, Major, Minor).</div></div>
                    <div class="faq-item"><div class="question">How to track bandwidth usage? <i class="fas fa-chevron-down"></i></div><div class="answer">Go to Network Ops → Bandwidth tab to see total usage, monthly cap, and daily usage charts.</div></div>
                    <div class="faq-item"><div class="question">How to generate an invoice? <i class="fas fa-chevron-down"></i></div><div class="answer">Go to Billing → Click "New Invoice" → Select customer → Enter amount and due date → Save.</div></div>
                </div>
            </section>

            <!-- ACTIVITY LOGS -->
            <section class="page" id="page-activity">
                <div class="flex-between" style="margin-bottom:18px;"><h3 style="font-weight:700;">Activity Logs</h3><button class="btn btn-outline btn-sm" id="clearLogsBtn"><i class="fas fa-trash"></i> Clear Logs</button></div>
                <div class="card"><div class="table-wrap"><table><thead><tr><th>Time</th><th>User</th><th>Action</th><th>Details</th></tr></thead><tbody id="activityLogBody"></tbody></table></div></div>
            </section>

            <!-- ============================================================ -->
            <!-- CUSTOMER PAGES -->
            <!-- ============================================================ -->
            <section class="page" id="page-c-dashboard">
                <div class="stats-grid">
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-box"></i> My Package</span><span class="icon-circle"><i class="fas fa-wifi"></i></span></div><div class="value" id="cPkgName">-</div><div class="change" id="cPkgSpeed">-</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-credit-card"></i> Due Amount</span><span class="icon-circle"><i class="fas fa-dollar-sign"></i></span></div><div class="value" id="cDueAmount">$0</div><div class="change negative">Pending</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-ticket-alt"></i> My Tickets</span><span class="icon-circle"><i class="fas fa-ticket"></i></span></div><div class="value" id="cTicketCount">0</div><div class="change" id="cTicketStatus">Open</div></div>
                    <div class="stat-card"><div class="top-row"><span class="label"><i class="fas fa-database"></i> Data Used</span><span class="icon-circle"><i class="fas fa-cloud"></i></span></div><div class="value" id="cDataUsed">0 GB</div><div class="change" id="cDataPercent">0%</div></div>
                </div>
                <div class="card"><div class="card-header"><h3>Welcome back, <span id="cWelcomeName">Customer</span> 👋</h3></div><p style="color:var(--text-secondary);">Your current package is <strong id="cWelcomePkg">-</strong>. You have <strong id="cWelcomePending">0</strong> pending invoices.</p></div>
                <div class="card"><div class="card-header"><h3>Bandwidth Usage (Last 7 Days)</h3></div><div class="chart-container" style="height:180px;"><canvas id="bandwidthChart"></canvas></div></div>
                <div class="card"><div class="card-header"><h3>Recent Activity</h3></div><div class="table-wrap"><table><thead><tr><th>Date</th><th>Event</th><th>Status</th></tr></thead><tbody id="cRecentActivity"></tbody></table></div></div>
            </section>

            <section class="page" id="page-c-profile">
                <div class="card"><div class="card-header"><h3>My Profile</h3></div><div style="font-size:16px; line-height:2.4;"><div><span class="text-muted">Name</span> <strong id="cProfName">-</strong></div><div><span class="text-muted">Email</span> <strong id="cProfEmail">-</strong></div><div><span class="text-muted">Package</span> <strong id="cProfPkg">-</strong> <button class="btn btn-sm btn-outline" id="changePackageBtn"><i class="fas fa-edit"></i> Change</button></div><div><span class="text-muted">Data Used</span> <strong id="cProfData">-</strong></div><div><span class="text-muted">Status</span> <span id="cProfStatus" class="status-badge active">Active</span></div><div><span class="text-muted">Connection</span> <span id="cProfConnection" class="status-badge online">Online</span></div></div></div>
            </section>

            <section class="page" id="page-c-payments">
                <div class="card"><div class="card-header"><h3>My Payment History</h3></div><div class="table-wrap"><table><thead><tr><th>Invoice #</th><th>Amount</th><th>Due Date</th><th>Status</th><th>Action</th></tr></thead><tbody id="cPaymentTable"></tbody></table></div></div>
            </section>

            <section class="page" id="page-c-tickets">
                <div class="card"><div class="card-header"><h3>My Support Tickets</h3></div><div class="table-wrap"><table><thead><tr><th>Ticket ID</th><th>Subject</th><th>Status</th><th>Priority</th></tr></thead><tbody id="cTicketTable"></tbody></table></div></div>
            </section>

            <section class="page" id="page-c-submit">
                <div class="card">
                    <div class="card-header"><h3>Submit a Ticket</h3></div>
                    <div class="form-group">
                        <label>Subject</label>
                        <input type="text" id="cNewTicketSubject" placeholder="Brief summary of your issue..." required />
                    </div>
                    <div class="form-group">
                        <label>Priority</label>
                        <select id="cNewTicketPriority">
                            <option value="low">Low</option>
                            <option value="medium" selected>Medium</option>
                            <option value="high">High</option>
                        </select>
                    </div>
                    <button class="btn" id="cSubmitTicketBtn"><i class="fas fa-paper-plane"></i> Submit</button>
                </div>
            </section>
        </main>
    </div>

    <!-- ==================== MODAL ==================== -->
    <div class="modal-overlay" id="modalOverlay">
        <div class="modal-box">
            <h2 id="modalTitle">Add New</h2>
            <div class="sub" id="modalSub">Fill in the details below.</div>
            <div id="modalBody"></div>
            <div class="modal-actions">
                <button class="btn btn-outline" id="modalCancel">Cancel</button>
                <button class="btn" id="modalConfirm">Save</button>
            </div>
        </div>
    </div>

    <!-- ==================== TOAST ==================== -->
    <div id="toastContainer"></div>

    <!-- ================================================================ -->
    <!-- SCRIPT — FULLY WORKING WITH ALL FEATURES -->
    <!-- ================================================================ -->
    <script>
        (function() {
            'use strict';
            // ================================================================
            // DATA — with localStorage persistence
            // ================================================================
            const STORAGE_KEY = 'netsphere_pro_data_v6';
            let defaultData = {
                customers: [
                    { id: 1, name: 'Ram Sharma', email: 'ram@gmail.com', package: 'Fiber 100', status: 'active',
                        dataUsed: 120, connection: 'online', lat: 27.7172, lng: 85.3240 },
                    { id: 2, name: 'Sita Rai', email: 'sita@gmail.com', package: 'Fiber 200', status: 'active',
                        dataUsed: 85, connection: 'online', lat: 27.7000, lng: 85.3100 },
                    { id: 3, name: 'Hari KC', email: 'hari@gmail.com', package: 'Fiber 50', status: 'active',
                        dataUsed: 45, connection: 'offline', lat: 27.7300, lng: 85.3400 },
                    { id: 4, name: 'Gita Adhikari', email: 'gita@gmail.com', package: 'Fiber 100', status: 'inactive',
                        dataUsed: 0, connection: 'offline', lat: 27.7100, lng: 85.3000 },
                    { id: 5, name: 'Krishna Thapa', email: 'krishna@gmail.com', package: 'Fiber 200', status: 'active',
                        dataUsed: 200, connection: 'online', lat: 27.7250, lng: 85.3150 },
                    { id: 6, name: 'Pranjal Neupane', email: 'pranjal@gmail.com', package: 'Fiber 100', status: 'active',
                        dataUsed: 60, connection: 'online', lat: 27.6950, lng: 85.3050 },
                    { id: 7, name: 'Sunita Sharma', email: 'sunita@gmail.com', package: 'Fiber 50', status: 'active',
                        dataUsed: 30, connection: 'online', lat: 27.7400, lng: 85.3500 },
                ],
                nextCustomerId: 8,
                packages: [
                    { id: 1, name: 'Fiber 50', speed: '50 Mbps', price: 1200 },
                    { id: 2, name: 'Fiber 100', speed: '100 Mbps', price: 1500 },
                    { id: 3, name: 'Fiber 200', speed: '200 Mbps', price: 2200 },
                    { id: 4, name: 'Fiber 500', speed: '500 Mbps', price: 3500 },
                ],
                nextPackageId: 5,
                invoices: [
                    { id: 1, customer: 'Ram Sharma', amount: 1500, due: '2026-09-15', status: 'paid' },
                    { id: 2, customer: 'Sita Rai', amount: 2200, due: '2026-09-20', status: 'paid' },
                    { id: 3, customer: 'Hari KC', amount: 1200, due: '2026-09-10', status: 'unpaid' },
                    { id: 4, customer: 'Gita Adhikari', amount: 1500, due: '2026-09-25', status: 'unpaid' },
                    { id: 5, customer: 'Krishna Thapa', amount: 2200, due: '2026-09-18', status: 'paid' },
                    { id: 6, customer: 'Pranjal Neupane', amount: 1500, due: '2026-09-28', status: 'unpaid' },
                ],
                nextInvoiceId: 7,
                tickets: [
                    { id: 1, customer: 'Ram Sharma', subject: 'Slow internet speed', status: 'open', priority: 'high' },
                    { id: 2, customer: 'Sita Rai', subject: 'Connection drop', status: 'closed', priority: 'medium' },
                    { id: 3, customer: 'Hari KC', subject: 'Billing question', status: 'open', priority: 'low' },
                    { id: 4, customer: 'Krishna Thapa', subject: 'Router configuration', status: 'open',
                    priority: 'medium' },
                    { id: 5, customer: 'Pranjal Neupane', subject: 'Downgrade package', status: 'open',
                    priority: 'low' },
                ],
                nextTicketId: 6,
                staff: [
                    { id: 1, name: 'Amit Shah', email: 'amit@netsphere.com', role: 'Technician', status: 'active' },
                    { id: 2, name: 'Rita Gurung', email: 'rita@netsphere.com', role: 'Support Lead', status: 'active' },
                    { id: 3, name: 'Suresh Pandey', email: 'suresh@netsphere.com', role: 'Billing Specialist',
                        status: 'active' },
                ],
                nextStaffId: 4,
                activityLogs: [],
                routers: [
                    { id: 1, name: 'Core-RTR-01', type: 'Core Router', mac: 'AA:BB:CC:DD:EE:01', firmware: 'v3.2.1',
                        uptime: '142d 7h', status: 'online' },
                    { id: 2, name: 'Switch-A-01', type: 'Switch', mac: 'AA:BB:CC:DD:EE:02', firmware: 'v2.8.4',
                        uptime: '89d 12h', status: 'online' },
                    { id: 3, name: 'Switch-B-01', type: 'Switch', mac: 'AA:BB:CC:DD:EE:03', firmware: 'v2.8.4',
                        uptime: '12d 3h', status: 'online' },
                    { id: 4, name: 'AP-1', type: 'Access Point', mac: 'AA:BB:CC:DD:EE:04', firmware: 'v1.5.2',
                        uptime: '45d 2h', status: 'online' },
                    { id: 5, name: 'AP-2', type: 'Access Point', mac: 'AA:BB:CC:DD:EE:05', firmware: 'v1.5.2',
                        uptime: '45d 2h', status: 'online' },
                    { id: 6, name: 'AP-3', type: 'Access Point', mac: 'AA:BB:CC:DD:EE:06', firmware: 'v1.4.9',
                        uptime: '2h 15m', status: 'offline' },
                    { id: 7, name: 'AP-4', type: 'Access Point', mac: 'AA:BB:CC:DD:EE:07', firmware: 'v1.5.2',
                        uptime: '30d 8h', status: 'online' },
                    { id: 8, name: 'AP-5', type: 'Access Point', mac: 'AA:BB:CC:DD:EE:08', firmware: 'v1.5.2',
                        uptime: '30d 8h', status: 'online' },
                ],
                bandwidthUsage: [45, 52, 38, 65, 70, 55, 48, 72, 68, 55, 60, 78, 85, 60, 52, 45, 70, 80, 55, 65, 72, 58, 50,
                    45, 60, 55, 48, 65, 70, 55
                ],
                totalBandwidthUsed: 1850,
                monthlyCap: 500
            };

            function loadData() {
                try {
                    const stored = localStorage.getItem(STORAGE_KEY);
                    if (stored) {
                        const parsed = JSON.parse(stored);
                        for (let key in defaultData) {
                            if (!(key in parsed)) parsed[key] = defaultData[key];
                        }
                        return parsed;
                    }
                } catch (e) {}
                return JSON.parse(JSON.stringify(defaultData));
            }

            function saveData() {
                try {
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
                } catch (e) {}
            }

            let data = loadData();
            let customers = data.customers;
            let packages = data.packages;
            let invoices = data.invoices;
            let tickets = data.tickets;
            let staff = data.staff;
            let activityLogs = data.activityLogs;
            let routers = data.routers || [];
            let bandwidthUsage = data.bandwidthUsage || [];
            let totalBandwidthUsed = data.totalBandwidthUsed || 0;
            let monthlyCap = data.monthlyCap || 500;
            let nextCustomerId = data.nextCustomerId;
            let nextPackageId = data.nextPackageId;
            let nextInvoiceId = data.nextInvoiceId;
            let nextTicketId = data.nextTicketId;
            let nextStaffId = data.nextStaffId;

            // ================================================================
            // STATE
            // ================================================================
            let currentUser = null;
            let currentCustomerName = null;
            let isDarkMode = false;
            let chartInstances = {};
            let customerPage = 1;
            const customerPageSize = 5;
            let selectedCustomers = new Set();
            let mapInstance = null;
            let sessionTimer;

            // ================================================================
            // DOM REFS
            // ================================================================
            const loginPage = document.getElementById('loginPage');
            const appContainer = document.getElementById('appContainer');
            const loginBtn = document.getElementById('loginBtn');
            const loginRole = document.getElementById('loginRole');
            const loginUser = document.getElementById('loginUser');
            const loginPass = document.getElementById('loginPass');
            const loginError = document.getElementById('loginError');
            const signOutBtn = document.getElementById('signOutBtn');
            const themeToggle = document.getElementById('themeToggle');
            const registerLink = document.getElementById('registerLink');
            const forgotPassword = document.getElementById('forgotPassword');
            const sidebar = document.getElementById('sidebar');

            // ================================================================
            // TOAST
            // ================================================================
            function showToast(message, type, duration) {
                type = type || 'info';
                duration = duration || 3500;
                const container = document.getElementById('toastContainer');
                const iconMap = { info: 'fa-info-circle', success: 'fa-check-circle', error: 'fa-exclamation-circle',
                    warning: 'fa-exclamation-triangle' };
                const toast = document.createElement('div');
                toast.className = 'toast ' + type;
                toast.innerHTML = '<i class="fas ' + (iconMap[type] || iconMap.info) + '"></i><span>' + message +
                    '</span><span class="toast-close"><i class="fas fa-times"></i></span>';
                container.appendChild(toast);
                const closeBtn = toast.querySelector('.toast-close');
                closeBtn.addEventListener('click', function() { toast.remove(); });
                setTimeout(function() { if (toast.parentNode) toast.remove(); }, duration);
            }

            // ================================================================
            // ACTIVITY LOGS
            // ================================================================
            function logActivity(user, action, details) {
                const entry = { time: new Date().toLocaleString(), user: user || 'System', action: action,
                details: details || '' };
                activityLogs.unshift(entry);
                if (activityLogs.length > 1000) activityLogs.pop();
                data.activityLogs = activityLogs;
                saveData();
                renderActivityLogs();
            }

            function renderActivityLogs() {
                const tbody = document.getElementById('activityLogBody');
                if (!tbody) return;
                tbody.innerHTML = activityLogs.slice(0, 50).map(function(log) {
                    return '<tr><td>' + log.time + '</td><td>' + log.user + '</td><td>' + log.action +
                        '</td><td>' + log.details + '</td></tr>';
                }).join('');
            }

            // ================================================================
            // SESSION TIMEOUT
            // ================================================================
            function resetSessionTimer() {
                clearTimeout(sessionTimer);
                sessionTimer = setTimeout(function() {
                    showToast('Session expired. Please login again.', 'warning');
                    logout();
                }, 30 * 60 * 1000);
            }
            document.addEventListener('click', resetSessionTimer);
            document.addEventListener('keydown', resetSessionTimer);
            document.addEventListener('mousemove', resetSessionTimer);

            // ================================================================
            // THEME TOGGLE
            // ================================================================
            themeToggle.addEventListener('click', function() {
                isDarkMode = !isDarkMode;
                document.body.classList.toggle('dark-mode', isDarkMode);
                this.innerHTML = isDarkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
                showToast(isDarkMode ? 'Light mode' : 'Dark mode', 'info');
            });

            // ================================================================
            // KEYBOARD SHORTCUTS
            // ================================================================
            document.addEventListener('keydown', function(e) {
                if (e.ctrlKey && e.key === 'n') {
                    e.preventDefault();
                    if (document.getElementById('page-customers').classList.contains('active')) {
                        openCustomerModal(null);
                    } else {
                        showToast('Switch to Customers page first', 'info');
                    }
                }
                if (e.ctrlKey && e.key === 's') {
                    e.preventDefault();
                    const confirmBtn = document.getElementById('modalConfirm');
                    if (document.getElementById('modalOverlay').classList.contains('open')) {
                        confirmBtn.click();
                    }
                }
                if (e.ctrlKey && e.key === 'f') {
                    e.preventDefault();
                    const search = document.getElementById('customerSearch');
                    if (search) { search.focus();
                        search.select(); }
                }
                if (e.key === 'Escape') {
                    if (document.getElementById('modalOverlay').classList.contains('open')) {
                        document.getElementById('modalCancel').click();
                    }
                }
            });

            // ================================================================
            // HELPERS
            // ================================================================
            function getPackageDistribution() {
                const dist = {};
                customers.forEach(function(c) { dist[c.package] = (dist[c.package] || 0) + 1; });
                return dist;
            }

            function getRecentPayments() {
                return invoices.slice(0, 5).map(function(inv) {
                    return { receipt: 'RCT-00' + inv.id, customer: inv.customer, amount: inv.amount,
                        status: inv.status };
                });
            }

            function getTotalRevenue() {
                return invoices.reduce(function(sum, inv) { return inv.status === 'paid' ? sum + inv.amount : sum; }, 0);
            }

            function getCustomerByName(name) {
                return customers.find(function(c) { return c.name === name; });
            }

            function getCustomerInvoices(name) {
                return invoices.filter(function(i) { return i.customer === name; });
            }

            function getCustomerTickets(name) {
                return tickets.filter(function(t) { return t.customer === name; });
            }
            const monthLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
            const revenueData = [3200, 2800, 4100, 3800, 5200, 4900];
            const growthData = [10, 15, 20, 18, 25, 30];

            function generateBandwidthData() {
                return Array.from({ length: 7 }, function() { return Math.floor(Math.random() * 150) + 20; });
            }

            // ================================================================
            // LOGIN AUTO-FILL
            // ================================================================
            loginRole.addEventListener('change', function() {
                if (this.value === 'admin') {
                    loginUser.value = 'admin';
                    loginPass.value = 'admin';
                } else {
                    loginUser.value = 'customer';
                    loginPass.value = 'customer';
                }
            });

            // ================================================================
            // RENDER FUNCTIONS — ADMIN
            // ================================================================
            function renderAdminStats() {
                const activeCustomers = customers.filter(function(c) { return c.status === 'active'; }).length;
                document.getElementById('statCustomers').textContent = customers.length;
                document.getElementById('statConnections').textContent = activeCustomers;
                document.getElementById('statTickets').textContent = tickets.filter(function(t) { return t.status ===
                    'open'; }).length;
                document.getElementById('statRevenue').textContent = '$' + getTotalRevenue().toLocaleString();
                document.getElementById('reportTotalRevenue').textContent = '$' + getTotalRevenue().toLocaleString();
                document.getElementById('reportCustomerGrowth').textContent = customers.length;
            }

            function renderAdminSnapshot() {
                document.getElementById('snapPackages').textContent = packages.length;
                document.getElementById('snapPending').textContent = invoices.filter(function(i) { return i.status ===
                    'unpaid' || i.status === 'overdue'; }).length;
                document.getElementById('snapOpenTickets').textContent = tickets.filter(function(t) { return t.status ===
                    'open'; }).length;
                document.getElementById('snapStaff').textContent = staff.length;
                document.getElementById('snapRevenueYTD').textContent = '$' + getTotalRevenue().toLocaleString();
            }

            function renderAdminRecentPayments() {
                const tbody = document.getElementById('recentPayments');
                const data = getRecentPayments();
                tbody.innerHTML = data.map(function(p) {
                    return '<tr><td><strong>' + p.receipt + '</strong></td><td>' + p.customer +
                        '</td><td>$' + p.amount.toLocaleString() + '</td><td><span class="status-badge ' +
                        p.status + '">' + p.status.toUpperCase() + '</span></td></tr>';
                }).join('');
            }

            function renderAdminCustomers(filter, pkgFilter, statusFilter) {
                filter = filter || '';
                pkgFilter = pkgFilter || '';
                statusFilter = statusFilter || '';
                const tbody = document.getElementById('customerTableBody');
                const q = filter.toLowerCase();
                let list = customers.filter(function(c) {
                    const matchName = c.name.toLowerCase().includes(q) || c.email.toLowerCase().includes(q);
                    const matchPkg = pkgFilter ? c.package === pkgFilter : true;
                    const matchStatus = statusFilter ? c.status === statusFilter : true;
                    return matchName && matchPkg && matchStatus;
                });
                const totalPages = Math.ceil(list.length / customerPageSize) || 1;
                const start = (customerPage - 1) * customerPageSize;
                const pageItems = list.slice(start, start + customerPageSize);

                tbody.innerHTML = pageItems.map(function(c) {
                    const dataUsedGB = (c.dataUsed || 0).toFixed(1);
                    const connStatus = c.connection || 'offline';
                    const checked = selectedCustomers.has(c.id) ? 'checked' : '';
                    return '<tr><td class="checkbox-cell"><input type="checkbox" class="customer-checkbox" data-id="' +
                        c.id + '" ' + checked +
                        '/></td><td><strong>' + c.name + '</strong></td><td>' + c.email + '</td><td>' + c
                        .package + '</td><td>' + dataUsedGB + ' GB</td><td><span class="status-badge ' + c
                        .status + '">' + c.status.toUpperCase() +
                        '</span></td><td><span class="status-badge ' + connStatus + '">' + connStatus
                        .toUpperCase() +
                        '</span></td><td><div class="action-group"><button class="btn btn-sm btn-outline" onclick="window.editCustomer(' +
                        c.id + ')"><i class="fas fa-edit"></i></button><button class="btn btn-sm btn-danger" onclick="window.deleteCustomer(' +
                        c.id + ')"><i class="fas fa-trash"></i></button></div></td></tr>';
                }).join('');

                updateBulkActions();

                const pag = document.getElementById('customerPagination');
                let html =
                    '<button class="page-btn ' + (customerPage <= 1 ? 'disabled' : '') +
                    '" onclick="window.changeCustomerPage(-1)"><i class="fas fa-chevron-left"></i></button>';
                for (var i = 1; i <= totalPages; i++) {
                    html += '<button class="page-btn ' + (i === customerPage ? 'active' : '') +
                        '" onclick="customerPage=' + i +
                        ';renderAdminCustomers(document.getElementById(\'customerSearch\').value, document.getElementById(\'filterPackage\').value, document.getElementById(\'filterStatus\').value);">' +
                        i + '</button>';
                }
                html += '<button class="page-btn ' + (customerPage >= totalPages ? 'disabled' : '') +
                    '" onclick="window.changeCustomerPage(1)"><i class="fas fa-chevron-right"></i></button>';
                pag.innerHTML = html;

                // Attach checkbox events
                document.querySelectorAll('.customer-checkbox').forEach(function(cb) {
                    cb.addEventListener('change', function() {
                        var id = parseInt(this.dataset.id);
                        if (this.checked) selectedCustomers.add(id);
                        else selectedCustomers.delete(id);
                        updateBulkActions();
                        updateSelectAllState();
                    });
                });

                // Select all
                document.getElementById('selectAllCustomers').addEventListener('change', function() {
                    var checked = this.checked;
                    document.querySelectorAll('.customer-checkbox').forEach(function(cb) {
                        cb.checked = checked;
                        var id = parseInt(cb.dataset.id);
                        if (checked) selectedCustomers.add(id);
                        else selectedCustomers.delete(id);
                    });
                    updateBulkActions();
                });
            }

            function updateBulkActions() {
                var bar = document.getElementById('bulkActionsBar');
                var count = document.getElementById('bulkCount');
                if (selectedCustomers.size > 0) {
                    bar.classList.add('visible');
                    count.textContent = selectedCustomers.size + ' selected';
                } else {
                    bar.classList.remove('visible');
                }
            }

            function updateSelectAllState() {
                var checkboxes = document.querySelectorAll('.customer-checkbox');
                var checked = document.querySelectorAll('.customer-checkbox:checked');
                var selectAll = document.getElementById('selectAllCustomers');
                if (checkboxes.length > 0) { selectAll.checked = checked.length === checkboxes.length; }
            }

            window.changeCustomerPage = function(delta) {
                var q = document.getElementById('customerSearch').value;
                var pkg = document.getElementById('filterPackage').value;
                var status = document.getElementById('filterStatus').value;
                var list = customers.filter(function(c) {
                    var matchName = c.name.toLowerCase().includes(q.toLowerCase()) || c.email.toLowerCase()
                        .includes(q.toLowerCase());
                    var matchPkg = pkg ? c.package === pkg : true;
                    var matchStatus = status ? c.status === status : true;
                    return matchName && matchPkg && matchStatus;
                });
                var totalPages = Math.ceil(list.length / customerPageSize) || 1;
                customerPage = Math.max(1, Math.min(totalPages, customerPage + delta));
                renderAdminCustomers(q, pkg, status);
            };

            document.getElementById('bulkDeleteBtn').addEventListener('click', function() {
                if (selectedCustomers.size === 0) { showToast('No customers selected.', 'warning'); return; }
                if (confirm('Delete ' + selectedCustomers.size + ' customers?')) {
                    customers = customers.filter(function(c) { return !selectedCustomers.has(c.id); });
                    data.customers = customers;
                    logActivity(currentUser || 'Admin', 'Bulk Delete', 'Deleted ' + selectedCustomers.size +
                        ' customers');
                    selectedCustomers.clear();
                    renderAdminAll();
                    showToast('Deleted customers successfully', 'success');
                }
            });

            document.getElementById('bulkClearBtn').addEventListener('click', function() {
                selectedCustomers.clear();
                document.querySelectorAll('.customer-checkbox').forEach(function(cb) { cb.checked = false; });
                updateBulkActions();
            });

            function renderAdminPackages() {
                var grid = document.getElementById('packageGrid');
                grid.innerHTML = packages.map(function(p) {
                    return '<div class="pkg-card"><div class="pkg-name">' + p.name + '</div><div class="pkg-speed">' +
                        p.speed + '</div><div class="pkg-price">$' + p.price.toLocaleString() +
                        ' <small>/mo</small></div><button class="btn btn-sm btn-outline" onclick="window.editPackage(' +
                        p.id + ')"><i class="fas fa-edit"></i> Manage</button><button class="btn btn-sm btn-danger" style="margin-top:4px;" onclick="window.deletePackage(' +
                        p.id + ')"><i class="fas fa-trash"></i></button></div>';
                }).join('');
            }

            function renderAdminBilling() {
                var tbody = document.getElementById('billingTableBody');
                tbody.innerHTML = invoices.map(function(inv) {
                    var actions = '';
                    if (inv.status === 'unpaid' || inv.status === 'overdue') {
                        actions +=
                            '<button class="btn btn-sm btn-success" onclick="window.markPaid(' + inv.id +
                            ')"><i class="fas fa-check"></i> Pay</button>';
                    }
                    actions +=
                        '<button class="btn btn-sm btn-outline" onclick="window.downloadPDFInvoice(' + inv.id +
                        ')"><i class="fas fa-file-pdf"></i> PDF</button>';
                    actions +=
                        '<button class="btn btn-sm btn-danger" onclick="window.deleteInvoice(' + inv.id +
                        ')"><i class="fas fa-trash"></i></button>';
                    return '<tr><td><strong>#INV-' + String(inv.id).padStart(4, '0') +
                        '</strong></td><td>' + inv.customer + '</td><td>$' + inv.amount.toLocaleString() +
                        '</td><td>' + inv.due + '</td><td><span class="status-badge ' + inv.status +
                        '">' + inv.status.toUpperCase() +
                        '</span></td><td><div class="action-group">' + actions + '</div></td></tr>';
                }).join('');
            }

            function renderAdminTickets() {
                var tbody = document.getElementById('ticketTableBody');
                tbody.innerHTML = tickets.map(function(t) {
                    return '<tr><td><strong>#TCK-' + String(t.id).padStart(4, '0') +
                        '</strong></td><td>' + t.customer + '</td><td>' + t.subject +
                        '</td><td><span class="status-badge ' + t.status + '">' + t.status.toUpperCase() +
                        '</span></td><td><span class="status-badge ' + t.priority + '">' + t.priority
                        .toUpperCase() +
                        '</span></td><td><div class="action-group"><button class="btn btn-sm btn-warning" onclick="window.toggleTicket(' +
                        t.id + ')"><i class="fas fa-sync"></i> Toggle</button><button class="btn btn-sm btn-danger" onclick="window.deleteTicket(' +
                        t.id + ')"><i class="fas fa-trash"></i></button></div></td></tr>';
                }).join('');
            }

            function renderAdminStaff() {
                var tbody = document.getElementById('staffTableBody');
                tbody.innerHTML = staff.map(function(s) {
                    return '<tr><td><strong>' + s.name + '</strong></td><td>' + s.email + '</td><td>' + s
                        .role + '</td><td><span class="status-badge ' + s.status + '">' + s.status
                        .toUpperCase() +
                        '</span></td><td><div class="action-group"><button class="btn btn-sm btn-outline" onclick="window.editStaff(' +
                        s.id + ')"><i class="fas fa-edit"></i></button><button class="btn btn-sm btn-danger" onclick="window.deleteStaff(' +
                        s.id + ')"><i class="fas fa-trash"></i></button></div></td></tr>';
                }).join('');
            }

            function renderNetworkOps() {
                var onlineDevices = routers.filter(function(r) { return r.status === 'online'; }).length;
                var totalDevices = routers.length;
                document.getElementById('netDevices').textContent = totalDevices;
                var usedIPs = customers.filter(function(c) { return c.connection === 'online'; }).length;
                var totalIPs = 256;
                document.getElementById('netIPUsage').textContent = Math.round((usedIPs / totalIPs) * 100) + '%';
                var outageCount = 3;
                document.getElementById('netOutages').textContent = outageCount;
                document.getElementById('netOutageStatus').textContent = outageCount > 0 ? outageCount + ' active' :
                    'No outages';
                document.getElementById('netBandwidth').textContent = Math.round(Math.random() * 200 + 50) + ' Mbps';
                renderIPPool();
                renderRouters();
                renderBandwidthTab();
                renderOutages();
            }

            function renderIPPool() {
                var grid = document.getElementById('ipPoolGrid');
                if (!grid) return;
                var totalIPs = 256;
                var usedIPs = customers.filter(function(c) { return c.connection === 'online'; }).length;
                var available = totalIPs - usedIPs - 10;
                document.getElementById('ipTotal').textContent = totalIPs;
                document.getElementById('ipAvailable').textContent = available;
                document.getElementById('ipAssigned').textContent = usedIPs;
                var ips = [];
                for (var i = 1; i <= 40; i++) {
                    var status = 'available';
                    var label = '192.168.1.' + i;
                    if (i <= usedIPs) { status = 'assigned';
                        label = '192.168.1.' + i; } else if (i > usedIPs && i <= usedIPs + 10) { status = 'reserved';
                        label = '192.168.1.' + i; }
                    ips.push({ ip: label, status: status });
                }
                grid.innerHTML = ips.map(function(ip) {
                    return '<div class="ip-item"><span class="ip-address">' + ip.ip +
                        '</span><span class="ip-status ' + ip.status + '">' + ip.status + '</span></div>';
                }).join('');
            }

            function renderRouters() {
                var tbody = document.getElementById('routerTableBody');
                if (!tbody) return;
                tbody.innerHTML = routers.map(function(r) {
                    return '<tr><td><strong>' + r.name + '</strong></td><td>' + r.type + '</td><td>' + r
                        .mac + '</td><td>' + r.firmware + '</td><td>' + r.uptime +
                        '</td><td><span class="status-badge ' + r.status + '">' + r.status.toUpperCase() +
                        '</span></td></tr>';
                }).join('');
            }

            function renderBandwidthTab() {
                var totalUsed = totalBandwidthUsed || 0;
                var cap = monthlyCap || 500;
                var percent = Math.min(100, (totalUsed / cap) * 100);
                document.getElementById('bandwidthTotal').textContent = totalUsed.toFixed(1) + ' GB';
                document.getElementById('bandwidthPercent').textContent = percent.toFixed(0) + '% of cap';
                document.getElementById('bandwidthRemaining').textContent = (cap - totalUsed).toFixed(1) + ' GB';
                document.getElementById('bandwidthBar').style.width = percent + '%';
                if (percent > 80) { document.getElementById('bandwidthBar').style.background = 'var(--danger)'; } else if (
                    percent > 60) { document.getElementById('bandwidthBar').style.background = 'var(--warning)'; }

                var ctx = document.getElementById('bandwidthUsageChart')?.getContext('2d');
                if (ctx) {
                    if (chartInstances.bandwidthUsage) { chartInstances.bandwidthUsage.destroy(); }
                    var labels = bandwidthUsage.length > 0 ? bandwidthUsage.map(function(_, i) { return 'Day ' + (i +
                        1); }) : ['No data'];
                    var dataValues = bandwidthUsage.length > 0 ? bandwidthUsage : [0];
                    chartInstances.bandwidthUsage = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: labels.slice(0, 30),
                            datasets: [{ label: 'Daily Usage (GB)', data: dataValues.slice(0, 30),
                                backgroundColor: 'rgba(99, 102, 241, 0.4)', borderColor: '#6366f1',
                                borderWidth: 1, }]
                        },
                        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
                            scales: { y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.02)' },
                                    ticks: { color: '#64748b' } }, x: { grid: { display: false },
                                    ticks: { color: '#64748b', font: { size: 9 } } } } }
                    });
                }
            }

            function renderOutages() {
                var summary = document.getElementById('outageSummary');
                if (summary) summary.textContent = '3 active outages · 17 customers affected';
            }

            function updateAdminBadges() {
                document.getElementById('customerBadge').textContent = customers.length;
                document.getElementById('billingBadge').textContent = invoices.filter(function(i) { return i.status ===
                    'unpaid' || i.status === 'overdue'; }).length;
                document.getElementById('ticketBadge').textContent = tickets.filter(function(t) { return t.status ===
                    'open'; }).length;
                document.getElementById('notifDot').textContent = invoices.filter(function(i) { return i.status ===
                    'unpaid' || i.status === 'overdue'; }).length + tickets.filter(function(t) { return t.status ===
                    'open'; }).length;
            }

            function renderAdminAll() {
                renderAdminStats();
                renderAdminRecentPayments();
                renderAdminCustomers(document.getElementById('customerSearch')?.value || '');
                renderAdminPackages();
                renderAdminBilling();
                renderAdminTickets();
                renderAdminStaff();
                renderAdminSnapshot();
                renderAdminCharts();
                renderReportCharts();
                renderNetworkOps();
                updateAdminBadges();
                renderActivityLogs();
                setTimeout(initMap, 400);
                saveData();
            }

            // ================================================================
            // CHARTS
            // ================================================================
            function renderAdminCharts() {
                var ctx1 = document.getElementById('revenueChart').getContext('2d');
                if (chartInstances.revenue) { chartInstances.revenue.destroy(); }
                chartInstances.revenue = new Chart(ctx1, {
                    type: 'line',
                    data: { labels: monthLabels, datasets: [{ label: 'Revenue ($)', data: revenueData,
                            borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true,
                            tension: 0.4, pointBackgroundColor: '#6366f1', pointRadius: 4,
                            pointHoverRadius: 6, }] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false },
                            tooltip: { backgroundColor: 'rgba(0,0,0,0.8)', titleColor: '#fff',
                                bodyColor: '#94a3b8' } }, scales: { y: { beginAtZero: true,
                                grid: { color: 'rgba(255,255,255,0.02)' }, ticks: { color: '#64748b',
                                    font: { size: 10 } } }, x: { grid: { display: false },
                                ticks: { color: '#64748b', font: { size: 10 } } } } }
                });
                var ctx2 = document.getElementById('packageChart').getContext('2d');
                if (chartInstances.package) { chartInstances.package.destroy(); }
                var dist = getPackageDistribution();
                var keys = Object.keys(dist);
                var colors = ['#6366f1', '#8b5cf6', '#06b6d4', '#10b981', '#f59e0b'];
                var dataValues = keys.map(function(k) { return dist[k]; });
                chartInstances.package = new Chart(ctx2, {
                    type: 'doughnut',
                    data: { labels: keys.length ? keys : ['No Data'], datasets: [{ data: keys.length ?
                            dataValues : [1], backgroundColor: keys.length ? colors.slice(0, keys
                                .length) : ['rgba(255,255,255,0.04)'], borderWidth: 2,
                            borderColor: 'rgba(0,0,0,0.4)', }] },
                    options: { responsive: true, maintainAspectRatio: false, cutout: '65%',
                    plugins: { legend: { position: 'right', labels: { boxWidth: 12, padding: 8,
                                color: '#94a3b8', font: { size: 10, weight: '500' } } },
                            tooltip: { callbacks: { label: function(context) { var total = context
                                        .dataset.data.reduce(function(a, b) { return a + b; }, 0);
                                    var pct = total > 0 ? Math.round((context.parsed / total) *
                                        100) : 0; return context.label + ': ' + context
                                        .parsed + ' (' + pct + '%)'; } } } } }
                });
            }

            function renderReportCharts() {
                var ctx1 = document.getElementById('revenueReportChart')?.getContext('2d');
                if (ctx1) {
                    if (chartInstances.revenueReport) { chartInstances.revenueReport.destroy(); }
                    chartInstances.revenueReport = new Chart(ctx1, {
                        type: 'bar',
                        data: { labels: monthLabels, datasets: [{ label: 'Revenue ($)', data: revenueData,
                                backgroundColor: 'rgba(99,102,241,0.3)', borderColor: '#6366f1',
                                borderWidth: 1, }] },
                        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
                            scales: { y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.02)' },
                                    ticks: { color: '#64748b' } }, x: { grid: { display: false },
                                    ticks: { color: '#64748b' } } } }
                    });
                }
                var ctx2 = document.getElementById('growthReportChart')?.getContext('2d');
                if (ctx2) {
                    if (chartInstances.growthReport) { chartInstances.growthReport.destroy(); }
                    chartInstances.growthReport = new Chart(ctx2, {
                        type: 'line',
                        data: { labels: monthLabels, datasets: [{ label: 'New Customers', data: growthData,
                                borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.06)',
                                fill: true, tension: 0.4, pointBackgroundColor: '#10b981',
                                pointRadius: 4, }] },
                        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
                            scales: { y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.02)' },
                                    ticks: { color: '#64748b' } }, x: { grid: { display: false },
                                    ticks: { color: '#64748b' } } } }
                    });
                }
            }

            function renderBandwidthChart() {
                var ctx = document.getElementById('bandwidthChart')?.getContext('2d');
                if (!ctx) return;
                if (chartInstances.bandwidth) { chartInstances.bandwidth.destroy(); }
                var data = generateBandwidthData();
                var days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
                chartInstances.bandwidth = new Chart(ctx, {
                    type: 'line',
                    data: { labels: days, datasets: [{ label: 'Bandwidth (GB)', data: data,
                            borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.10)',
                            fill: true, tension: 0.4, pointBackgroundColor: '#6366f1', pointRadius: 4,
                        }] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } },
                        scales: { y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.02)' },
                                ticks: { color: '#64748b' } }, x: { grid: { display: false },
                                ticks: { color: '#64748b' } } } }
                });
            }

            // ================================================================
            // CRUD OPERATIONS
            // ================================================================
            window.editCustomer = function(id) {
                var c = customers.find(function(x) { return x.id === id; });
                if (c) openCustomerModal(c);
            };
            window.deleteCustomer = function(id) {
                if (confirm('Delete this customer?')) {
                    var c = customers.find(function(x) { return x.id === id; });
                    customers = customers.filter(function(c) { return c.id !== id; });
                    data.customers = customers;
                    selectedCustomers.delete(id);
                    logActivity(currentUser || 'Admin', 'Deleted Customer', 'Deleted ' + (c ? c.name : 'unknown'));
                    renderAdminAll();
                    showToast('Customer deleted', 'success');
                }
            };

            function openCustomerModal(data) {
                var isEdit = !!data;
                var title = isEdit ? 'Edit Customer' : 'Add Customer';
                var sub = isEdit ? 'Update customer details.' : 'Enter customer details.';
                var nameVal = isEdit ? data.name : '';
                var emailVal = isEdit ? data.email : '';
                var pkgVal = isEdit ? data.package : packages[0]?.name || '';
                var statusVal = isEdit ? data.status : 'active';
                var dataUsedVal = isEdit ? data.dataUsed || 0 : 0;
                var connVal = isEdit ? data.connection || 'online' : 'online';
                var latVal = isEdit && data.lat ? data.lat : 27.7172;
                var lngVal = isEdit && data.lng ? data.lng : 85.3240;

                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalSub').textContent = sub;
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Full Name</label><input type="text" id="f_cust_name" value="' +
                    nameVal + '" required /></div><div class="form-group"><label>Email</label><input type="email" id="f_cust_email" value="' +
                    emailVal +
                    '" required /></div><div class="form-group"><label>Package</label><select id="f_cust_package">' +
                    packages.map(function(p) { return '<option value="' + p.name + '" ' + (p.name === pkgVal ?
                        'selected' : '') + '>' + p.name + '</option>'; }).join('') +
                    '</select></div><div class="form-group"><label>Data Used (GB)</label><input type="number" id="f_cust_data" value="' +
                    dataUsedVal + '" min="0" step="0.1" /></div><div class="form-group"><label>Status</label><select id="f_cust_status"><option value="active" ' +
                    (statusVal === 'active' ? 'selected' : '') +
                    '>Active</option><option value="inactive" ' + (statusVal === 'inactive' ? 'selected' : '') +
                    '>Inactive</option></select></div><div class="form-group"><label>Connection</label><select id="f_cust_connection"><option value="online" ' +
                    (connVal === 'online' ? 'selected' : '') +
                    '>Online</option><option value="offline" ' + (connVal === 'offline' ? 'selected' : '') +
                    '>Offline</option></select></div><div class="form-group"><label>Latitude (for map)</label><input type="number" id="f_cust_lat" value="' +
                    latVal +
                    '" step="0.0001" /></div><div class="form-group"><label>Longitude (for map)</label><input type="number" id="f_cust_lng" value="' +
                    lngVal + '" step="0.0001" /></div><div class="field-hint">All fields are required.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var name = document.getElementById('f_cust_name').value.trim();
                    var email = document.getElementById('f_cust_email').value.trim();
                    var pkg = document.getElementById('f_cust_package').value;
                    var status = document.getElementById('f_cust_status').value;
                    var dataUsed = parseFloat(document.getElementById('f_cust_data').value) || 0;
                    var connection = document.getElementById('f_cust_connection').value;
                    var lat = parseFloat(document.getElementById('f_cust_lat').value) || 27.7172;
                    var lng = parseFloat(document.getElementById('f_cust_lng').value) || 85.3240;
                    if (!name || !email) { showToast('Name and email are required.', 'error'); return; }
                    if (isEdit) {
                        var idx = customers.findIndex(function(c) { return c.id === data.id; });
                        if (idx > -1) {
                            customers[idx] = { id: data.id, name: name, email: email, package: pkg,
                                status: status, dataUsed: dataUsed, connection: connection, lat: lat,
                                lng: lng };
                            data.customers = customers;
                            logActivity(currentUser || 'Admin', 'Updated Customer', 'Updated ' + name +
                                ' (' + email + ')');
                        }
                    } else {
                        var newId = nextCustomerId++;
                        customers.push({ id: newId, name: name, email: email, package: pkg, status: status,
                            dataUsed: dataUsed, connection: connection, lat: lat, lng: lng });
                        data.customers = customers;
                        data.nextCustomerId = nextCustomerId;
                        logActivity(currentUser || 'Admin', 'Added Customer', 'Added ' + name + ' (' +
                            email + ')');
                    }
                    closeModal();
                    renderAdminAll();
                    showToast(isEdit ? 'Customer updated' : 'Customer added', 'success');
                };
            }
            // ---- PACKAGES ----
            window.editPackage = function(id) {
                var p = packages.find(function(x) { return x.id === id; });
                if (p) openPackageModal(p);
            };
            window.deletePackage = function(id) {
                if (confirm('Delete this package?')) {
                    var p = packages.find(function(x) { return x.id === id; });
                    packages = packages.filter(function(p) { return p.id !== id; });
                    data.packages = packages;
                    logActivity(currentUser || 'Admin', 'Deleted Package', 'Deleted ' + (p ? p.name : 'unknown'));
                    renderAdminAll();
                    showToast('Package deleted', 'warning');
                }
            };

            function openPackageModal(data) {
                var isEdit = !!data;
                var title = isEdit ? 'Edit Package' : 'Create Package';
                var sub = isEdit ? 'Update package details.' : 'Enter package details.';
                var nameVal = isEdit ? data.name : '';
                var speedVal = isEdit ? data.speed : '';
                var priceVal = isEdit ? data.price : '';
                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalSub').textContent = sub;
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Package Name</label><input type="text" id="f_pkg_name" value="' +
                    nameVal + '" required /></div><div class="form-group"><label>Speed</label><input type="text" id="f_pkg_speed" value="' +
                    speedVal +
                    '" required /></div><div class="form-group"><label>Price (per month)</label><input type="number" id="f_pkg_price" value="' +
                    priceVal +
                    '" required min="1" /></div><div class="field-hint">All fields are required. Price must be greater than 0.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var name = document.getElementById('f_pkg_name').value.trim();
                    var speed = document.getElementById('f_pkg_speed').value.trim();
                    var price = parseFloat(document.getElementById('f_pkg_price').value);
                    if (!name || !speed || isNaN(price) || price <= 0) { showToast(
                            'Please fill all fields correctly.', 'error'); return; }
                    if (isEdit) {
                        var idx = packages.findIndex(function(p) { return p.id === data.id; });
                        if (idx > -1) {
                            packages[idx] = { id: data.id, name: name, speed: speed, price: price };
                            data.packages = packages;
                            logActivity(currentUser || 'Admin', 'Updated Package', 'Updated ' + name);
                        }
                    } else {
                        var newId = nextPackageId++;
                        packages.push({ id: newId, name: name, speed: speed, price: price });
                        data.packages = packages;
                        data.nextPackageId = nextPackageId;
                        logActivity(currentUser || 'Admin', 'Added Package', 'Added ' + name);
                    }
                    closeModal();
                    renderAdminAll();
                    showToast(isEdit ? 'Package updated' : 'Package created', 'success');
                };
            }
            // ---- BILLING ----
            window.markPaid = function(id) {
                var inv = invoices.find(function(i) { return i.id === id; });
                if (inv) {
                    inv.status = 'paid';
                    data.invoices = invoices;
                    logActivity(currentUser || 'Admin', 'Marked Invoice Paid', 'Invoice #INV-' + String(id)
                        .padStart(4, '0'));
                    renderAdminAll();
                    showToast('Invoice marked as paid', 'success');
                }
            };
            window.deleteInvoice = function(id) {
                if (confirm('Delete this invoice?')) {
                    invoices = invoices.filter(function(i) { return i.id !== id; });
                    data.invoices = invoices;
                    logActivity(currentUser || 'Admin', 'Deleted Invoice', 'Invoice #INV-' + String(id).padStart(4,
                        '0'));
                    renderAdminAll();
                    showToast('Invoice deleted', 'warning');
                }
            };
            window.downloadPDFInvoice = function(id) {
                var inv = invoices.find(function(i) { return i.id === id; });
                if (!inv) { showToast('Invoice not found.', 'error'); return; }
                var doc = new jspdf.jsPDF();
                doc.setFontSize(20);
                doc.text('NetSphere Invoice', 20, 30);
                doc.setFontSize(12);
                doc.text('Invoice #: INV-' + String(inv.id).padStart(4, '0'), 20, 50);
                doc.text('Customer: ' + inv.customer, 20, 60);
                doc.text('Amount: $' + inv.amount.toLocaleString(), 20, 70);
                doc.text('Due Date: ' + inv.due, 20, 80);
                doc.text('Status: ' + inv.status.toUpperCase(), 20, 90);
                doc.text('Thank you for using NetSphere!', 20, 110);
                doc.save('invoice-' + inv.id + '.pdf');
                logActivity(currentUser || 'Admin', 'Downloaded PDF Invoice', 'Invoice #INV-' + String(id).padStart(4,
                    '0'));
                showToast('PDF invoice downloaded', 'success');
            };

            function openInvoiceModal(data) {
                var isEdit = !!data;
                var title = isEdit ? 'Edit Invoice' : 'New Invoice';
                var sub = isEdit ? 'Update invoice details.' : 'Create a new invoice.';
                var custVal = isEdit ? data.customer : (customers[0]?.name || '');
                var amtVal = isEdit ? data.amount : '';
                var dueVal = isEdit ? data.due : '';
                var statusVal = isEdit ? data.status : 'unpaid';
                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalSub').textContent = sub;
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Customer</label><select id="f_inv_customer">' + customers.map(
                        function(c) { return '<option value="' + c.name + '" ' + (c.name === custVal ?
                            'selected' : '') + '>' + c.name + '</option>'; }).join('') +
                    '</select></div><div class="form-group"><label>Amount ($)</label><input type="number" id="f_inv_amount" value="' +
                    amtVal +
                    '" required min="1" /></div><div class="form-group"><label>Due Date</label><input type="date" id="f_inv_due" value="' +
                    dueVal +
                    '" required /></div><div class="form-group"><label>Status</label><select id="f_inv_status"><option value="paid" ' +
                    (statusVal === 'paid' ? 'selected' : '') +
                    '>Paid</option><option value="unpaid" ' + (statusVal === 'unpaid' ? 'selected' : '') +
                    '>Unpaid</option></select></div><div class="field-hint">All fields are required.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var customer = document.getElementById('f_inv_customer').value;
                    var amount = parseFloat(document.getElementById('f_inv_amount').value);
                    var due = document.getElementById('f_inv_due').value;
                    var status = document.getElementById('f_inv_status').value;
                    if (!customer || isNaN(amount) || amount <= 0 || !due) { showToast(
                            'Please fill all fields.', 'error'); return; }
                    if (isEdit) {
                        var idx = invoices.findIndex(function(i) { return i.id === data.id; });
                        if (idx > -1) {
                            invoices[idx] = { id: data.id, customer: customer, amount: amount, due: due,
                                status: status };
                            data.invoices = invoices;
                            logActivity(currentUser || 'Admin', 'Updated Invoice', 'Invoice #INV-' +
                                String(data.id).padStart(4, '0'));
                        }
                    } else {
                        var newId = nextInvoiceId++;
                        invoices.push({ id: newId, customer: customer, amount: amount, due: due,
                            status: status });
                        data.invoices = invoices;
                        data.nextInvoiceId = nextInvoiceId;
                        logActivity(currentUser || 'Admin', 'Created Invoice', 'Invoice #INV-' + String(
                            newId).padStart(4, '0') + ' for ' + customer);
                    }
                    closeModal();
                    renderAdminAll();
                    showToast(isEdit ? 'Invoice updated' : 'Invoice created', 'success');
                };
            }
            // ---- TICKETS ----
            window.toggleTicket = function(id) {
                var t = tickets.find(function(x) { return x.id === id; });
                if (t) {
                    t.status = t.status === 'open' ? 'closed' : 'open';
                    data.tickets = tickets;
                    logActivity(currentUser || 'Admin', 'Toggled Ticket', 'Ticket #TCK-' + String(id).padStart(4,
                        '0') + ' -> ' + t.status.toUpperCase());
                    renderAdminAll();
                    showToast('Ticket ' + (t.status === 'open' ? 'reopened' : 'closed'), 'info');
                }
            };
            window.deleteTicket = function(id) {
                if (confirm('Delete this ticket?')) {
                    tickets = tickets.filter(function(t) { return t.id !== id; });
                    data.tickets = tickets;
                    logActivity(currentUser || 'Admin', 'Deleted Ticket', 'Ticket #TCK-' + String(id).padStart(4,
                        '0'));
                    renderAdminAll();
                    showToast('Ticket deleted', 'warning');
                }
            };

            function openTicketModal(data) {
                var isEdit = !!data;
                var title = isEdit ? 'Edit Ticket' : 'New Ticket';
                var sub = isEdit ? 'Update ticket details.' : 'Create a new support ticket.';
                var custVal = isEdit ? data.customer : (customers[0]?.name || '');
                var subjVal = isEdit ? data.subject : '';
                var statusVal = isEdit ? data.status : 'open';
                var priVal = isEdit ? data.priority : 'medium';
                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalSub').textContent = sub;
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Customer</label><select id="f_tkt_customer">' + customers.map(
                        function(c) { return '<option value="' + c.name + '" ' + (c.name === custVal ?
                            'selected' : '') + '>' + c.name + '</option>'; }).join('') +
                    '</select></div><div class="form-group"><label>Subject</label><input type="text" id="f_tkt_subject" value="' +
                    subjVal +
                    '" required /></div><div class="form-group"><label>Status</label><select id="f_tkt_status"><option value="open" ' +
                    (statusVal === 'open' ? 'selected' : '') +
                    '>Open</option><option value="closed" ' + (statusVal === 'closed' ? 'selected' : '') +
                    '>Closed</option></select></div><div class="form-group"><label>Priority</label><select id="f_tkt_priority"><option value="low" ' +
                    (priVal === 'low' ? 'selected' : '') +
                    '>Low</option><option value="medium" ' + (priVal === 'medium' ? 'selected' : '') +
                    '>Medium</option><option value="high" ' + (priVal === 'high' ? 'selected' : '') +
                    '>High</option></select></div><div class="field-hint">All fields are required.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var customer = document.getElementById('f_tkt_customer').value;
                    var subject = document.getElementById('f_tkt_subject').value.trim();
                    var status = document.getElementById('f_tkt_status').value;
                    var priority = document.getElementById('f_tkt_priority').value;
                    if (!customer || !subject) { showToast('Customer and subject are required.', 'error');
                        return; }
                    if (isEdit) {
                        var idx = tickets.findIndex(function(t) { return t.id === data.id; });
                        if (idx > -1) {
                            tickets[idx] = { id: data.id, customer: customer, subject: subject,
                                status: status, priority: priority };
                            data.tickets = tickets;
                            logActivity(currentUser || 'Admin', 'Updated Ticket', 'Ticket #TCK-' +
                                String(data.id).padStart(4, '0'));
                        }
                    } else {
                        var newId = nextTicketId++;
                        tickets.push({ id: newId, customer: customer, subject: subject, status: status,
                            priority: priority });
                        data.tickets = tickets;
                        data.nextTicketId = nextTicketId;
                        logActivity(currentUser || 'Admin', 'Created Ticket', 'Ticket #TCK-' + String(
                            newId).padStart(4, '0') + ' for ' + customer);
                    }
                    closeModal();
                    renderAdminAll();
                    showToast(isEdit ? 'Ticket updated' : 'Ticket created', 'success');
                };
            }
            // ---- STAFF ----
            window.editStaff = function(id) {
                var s = staff.find(function(x) { return x.id === id; });
                if (s) openStaffModal(s);
            };
            window.deleteStaff = function(id) {
                if (confirm('Delete this staff member?')) {
                    var s = staff.find(function(x) { return x.id === id; });
                    staff = staff.filter(function(s) { return s.id !== id; });
                    data.staff = staff;
                    logActivity(currentUser || 'Admin', 'Deleted Staff', 'Deleted ' + (s ? s.name : 'unknown'));
                    renderAdminAll();
                    showToast('Staff deleted', 'warning');
                }
            };

            function openStaffModal(data) {
                var isEdit = !!data;
                var title = isEdit ? 'Edit Staff' : 'Add Staff';
                var sub = isEdit ? 'Update staff details.' : 'Add a new staff member.';
                var nameVal = isEdit ? data.name : '';
                var emailVal = isEdit ? data.email : '';
                var roleVal = isEdit ? data.role : 'Technician';
                var statusVal = isEdit ? data.status : 'active';
                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalSub').textContent = sub;
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Full Name</label><input type="text" id="f_staff_name" value="' +
                    nameVal + '" required /></div><div class="form-group"><label>Email</label><input type="email" id="f_staff_email" value="' +
                    emailVal +
                    '" required /></div><div class="form-group"><label>Role</label><select id="f_staff_role"><option value="Technician" ' +
                    (roleVal === 'Technician' ? 'selected' : '') +
                    '>Technician</option><option value="Support Lead" ' + (roleVal === 'Support Lead' ?
                        'selected' : '') +
                    '>Support Lead</option><option value="Billing Specialist" ' + (roleVal ===
                        'Billing Specialist' ? 'selected' : '') +
                    '>Billing Specialist</option><option value="Manager" ' + (roleVal === 'Manager' ?
                        'selected' : '') + '>Manager</option></select></div><div class="form-group"><label>Status</label><select id="f_staff_status"><option value="active" ' +
                    (statusVal === 'active' ? 'selected' : '') +
                    '>Active</option><option value="inactive" ' + (statusVal === 'inactive' ? 'selected' : '') +
                    '>Inactive</option></select></div><div class="field-hint">All fields are required.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var name = document.getElementById('f_staff_name').value.trim();
                    var email = document.getElementById('f_staff_email').value.trim();
                    var role = document.getElementById('f_staff_role').value;
                    var status = document.getElementById('f_staff_status').value;
                    if (!name || !email) { showToast('Name and email are required.', 'error'); return; }
                    if (isEdit) {
                        var idx = staff.findIndex(function(s) { return s.id === data.id; });
                        if (idx > -1) {
                            staff[idx] = { id: data.id, name: name, email: email, role: role,
                                status: status };
                            data.staff = staff;
                            logActivity(currentUser || 'Admin', 'Updated Staff', 'Updated ' + name);
                        }
                    } else {
                        var newId = nextStaffId++;
                        staff.push({ id: newId, name: name, email: email, role: role, status: status });
                        data.staff = staff;
                        data.nextStaffId = nextStaffId;
                        logActivity(currentUser || 'Admin', 'Added Staff', 'Added ' + name);
                    }
                    closeModal();
                    renderAdminAll();
                    showToast(isEdit ? 'Staff updated' : 'Staff added', 'success');
                };
            }

            // ================================================================
            // BULK IMPORT / EXPORT
            // ================================================================
            document.getElementById('bulkImportBtn').addEventListener('click', function() {
                document.getElementById('modalTitle').textContent = 'Bulk Import Customers';
                document.getElementById('modalSub').textContent =
                    'Upload CSV file with columns: Name, Email, Package, Status, DataUsed, Connection, Lat, Lng';
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>CSV File</label><input type="file" id="csvFileInput" accept=".csv" /><div class="field-hint">File must have header row.</div></div><div class="form-group"><label>Sample Format</label><pre style="background:rgba(255,255,255,0.02);padding:10px;border-radius:var(--radius-xs);font-size:12px;color:var(--text-secondary);">Name,Email,Package,Status,DataUsed,Connection,Lat,Lng\nJohn Doe,john@test.com,Fiber 100,active,50,online,27.7172,85.3240</pre></div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var fileInput = document.getElementById('csvFileInput');
                    if (!fileInput.files || !fileInput.files[0]) { showToast('Please select a CSV file.',
                            'error'); return; }
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        var text = e.target.result;
                        var lines = text.split('\n').filter(function(line) { return line.trim() !==
                            ''; });
                        if (lines.length < 2) { showToast(
                                'File must have header and data rows.', 'error'); return; }
                        var headers = lines[0].split(',').map(function(h) { return h.trim(); });
                        var required = ['Name', 'Email', 'Package', 'Status'];
                        var missing = required.filter(function(r) { return !headers.includes(r); });
                        if (missing.length) { showToast('Missing columns: ' + missing.join(', '),
                                'error'); return; }
                        var added = 0;
                        for (var i = 1; i < lines.length; i++) {
                            var cols = lines[i].split(',').map(function(c) { return c.trim(); });
                            if (cols.length < headers.length) continue;
                            var row = {};
                            headers.forEach(function(h, idx) { row[h] = cols[idx] || ''; });
                            var name = row.Name,
                                email = row.Email,
                                pkg = row.Package,
                                status = row.Status.toLowerCase();
                            var dataUsed = parseFloat(row.DataUsed) || 0;
                            var connection = row.Connection?.toLowerCase() === 'online' ? 'online' :
                                'offline';
                            var lat = parseFloat(row.Lat) || 27.7172;
                            var lng = parseFloat(row.Lng) || 85.3240;
                            if (!name || !email || !pkg || !['active', 'inactive'].includes(status))
                                continue;
                            customers.push({ id: nextCustomerId++, name: name, email: email,
                                package: pkg, status: status, dataUsed: dataUsed,
                                connection: connection, lat: lat, lng: lng });
                            added++;
                        }
                        data.customers = customers;
                        data.nextCustomerId = nextCustomerId;
                        closeModal();
                        logActivity(currentUser || 'Admin', 'Bulk Import', 'Imported ' + added +
                            ' customers from CSV');
                        renderAdminAll();
                        showToast('Successfully imported ' + added + ' customers!', 'success');
                    };
                    reader.readAsText(fileInput.files[0]);
                };
            });

            document.getElementById('exportCsvBtn').addEventListener('click', function() {
                var headers = ['Name', 'Email', 'Package', 'Status', 'DataUsed', 'Connection', 'Lat', 'Lng'];
                var rows = customers.map(function(c) {
                    return [c.name, c.email, c.package, c.status, c.dataUsed || 0, c.connection || 'offline',
                        c.lat || 27.7172, c.lng || 85.3240
                    ];
                });
                var csvContent = [headers.join(',')].concat(rows.map(function(r) { return r.join(','); })).join(
                '\n');
                var blob = new Blob([csvContent], { type: 'text/csv' });
                var url = URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = 'customers.csv';
                a.click();
                URL.revokeObjectURL(url);
                logActivity(currentUser || 'Admin', 'Exported CSV', 'Exported customer list');
                showToast('Customers exported successfully', 'success');
            });

            document.getElementById('exportReportPdf')?.addEventListener('click', function() {
                var doc = new jspdf.jsPDF();
                doc.setFontSize(20);
                doc.text('NetSphere Report', 20, 30);
                doc.setFontSize(12);
                doc.text('Generated: ' + new Date().toLocaleString(), 20, 45);
                doc.text('Total Revenue: $' + getTotalRevenue().toLocaleString(), 20, 60);
                doc.text('Total Customers: ' + customers.length, 20, 70);
                doc.text('Active Connections: ' + customers.filter(function(c) { return c.status === 'active'; })
                    .length, 20, 80);
                doc.text('Open Tickets: ' + tickets.filter(function(t) { return t.status === 'open'; }).length, 20,
                    90);
                doc.text('--- Package Distribution ---', 20, 105);
                var dist = getPackageDistribution();
                var y = 115;
                for (var pkg in dist) {
                    doc.text(pkg + ': ' + dist[pkg] + ' subscribers', 20, y);
                    y += 10;
                }
                doc.save('report.pdf');
                logActivity(currentUser || 'Admin', 'Exported PDF Report', 'Downloaded report');
                showToast('Report exported as PDF', 'success');
            });

            document.getElementById('clearLogsBtn')?.addEventListener('click', function() {
                if (confirm('Clear all activity logs?')) {
                    activityLogs = [];
                    data.activityLogs = activityLogs;
                    saveData();
                    renderActivityLogs();
                    showToast('Logs cleared', 'warning');
                }
            });

            // ================================================================
            // NETWORK OPS TABS
            // ================================================================
            document.querySelectorAll('[data-net-tab]').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    document.querySelectorAll('[data-net-tab]').forEach(function(b) { b.classList.remove(
                            'active'); });
                    this.classList.add('active');
                    var tab = this.dataset.netTab;
                    document.querySelectorAll('.net-tab-content').forEach(function(el) { el.style.display =
                            'none'; });
                    var target = document.getElementById('net-tab-' + tab);
                    if (target) target.style.display = 'block';
                });
            });
            document.getElementById('refreshIPPoolBtn')?.addEventListener('click', function() { renderIPPool();
                showToast('IP Pool refreshed', 'success'); });
            document.getElementById('refreshRoutersBtn')?.addEventListener('click', function() { renderRouters();
                showToast('Router status refreshed', 'success'); });

            // ================================================================
            // AUTO-BILLING
            // ================================================================
            function checkAutoBilling() {
                var today = new Date();
                var updated = false;
                invoices.forEach(function(inv) {
                    if (inv.status === 'unpaid') {
                        var dueDate = new Date(inv.due);
                        if (dueDate < today) {
                            inv.status = 'overdue';
                            updated = true;
                        }
                    }
                });
                if (updated) {
                    data.invoices = invoices;
                    saveData();
                    showToast('Auto-billing: Some invoices are overdue.', 'warning');
                    renderAdminAll();
                }
            }
            setInterval(checkAutoBilling, 24 * 60 * 60 * 1000);

            // ================================================================
            // CUSTOMER RENDER
            // ================================================================
            function renderCustomerAll(name) {
                var c = getCustomerByName(name);
                if (!c) return;
                var invs = getCustomerInvoices(name);
                var tkts = getCustomerTickets(name);
                var due = invs.filter(function(i) { return i.status === 'unpaid' || i.status === 'overdue'; })
                    .reduce(function(s, i) { return s + i.amount; }, 0);
                document.getElementById('cPkgName').textContent = c.package;
                var pkg = packages.find(function(p) { return p.name === c.package; });
                document.getElementById('cPkgSpeed').textContent = pkg ? pkg.speed : '-';
                document.getElementById('cDueAmount').textContent = '$' + due.toLocaleString();
                document.getElementById('cTicketCount').textContent = tkts.length;
                var openCount = tkts.filter(function(t) { return t.status === 'open'; }).length;
                document.getElementById('cTicketStatus').textContent = openCount > 0 ? openCount + ' open' :
                    'All closed';
                var dataUsedGB = (c.dataUsed || 0).toFixed(1);
                document.getElementById('cDataUsed').textContent = dataUsedGB + ' GB';
                var pct = Math.min(100, ((c.dataUsed || 0) / 500) * 100);
                document.getElementById('cDataPercent').textContent = pct.toFixed(0) + '%';
                document.getElementById('cWelcomeName').textContent = name;
                document.getElementById('cWelcomePkg').textContent = c.package;
                document.getElementById('cWelcomePending').textContent = invs.filter(function(i) { return i.status ===
                        'unpaid' || i.status === 'overdue'; }).length;

                var acts = [];
                invs.slice(0, 3).forEach(function(i) { acts.push({ date: i.due, event: 'Invoice #INV-' + String(i
                        .id).padStart(4, '0'), status: i.status }); });
                tkts.slice(0, 3).forEach(function(t) { acts.push({ date: 'Today', event: 'Ticket #TCK-' + String(t
                        .id).padStart(4, '0'), status: t.status }); });
                acts.sort(function(a, b) { return a.date > b.date ? -1 : 1; });
                var tbody = document.getElementById('cRecentActivity');
                tbody.innerHTML = acts.slice(0, 5).map(function(a) {
                    return '<tr><td>' + a.date + '</td><td>' + a.event +
                        '</td><td><span class="status-badge ' + a.status + '">' + a.status.toUpperCase() +
                        '</span></td></tr>';
                }).join('');

                document.getElementById('cProfName').textContent = c.name;
                document.getElementById('cProfEmail').textContent = c.email;
                document.getElementById('cProfPkg').textContent = c.package;
                document.getElementById('cProfData').textContent = dataUsedGB + ' GB';
                document.getElementById('cProfStatus').textContent = c.status.toUpperCase();
                document.getElementById('cProfStatus').className = 'status-badge ' + c.status;
                var conn = c.connection || 'offline';
                document.getElementById('cProfConnection').textContent = conn.toUpperCase();
                document.getElementById('cProfConnection').className = 'status-badge ' + conn;

                var ptbl = document.getElementById('cPaymentTable');
                ptbl.innerHTML = invs.map(function(i) {
                    var action = '';
                    if (i.status === 'unpaid' || i.status === 'overdue') {
                        action =
                            '<button class="btn btn-sm btn-success" onclick="window.payCustomerInvoice(' +
                            i.id + ')"><i class="fas fa-credit-card"></i> Pay Now</button>';
                    } else {
                        action = '—';
                    }
                    return '<tr><td><strong>#INV-' + String(i.id).padStart(4, '0') +
                        '</strong></td><td>$' + i.amount.toLocaleString() + '</td><td>' + i.due +
                        '</td><td><span class="status-badge ' + i.status + '">' + i.status.toUpperCase() +
                        '</span></td><td>' + action + '</td></tr>';
                }).join('');

                var ttbl = document.getElementById('cTicketTable');
                ttbl.innerHTML = tkts.map(function(t) {
                    return '<tr><td><strong>#TCK-' + String(t.id).padStart(4, '0') +
                        '</strong></td><td>' + t.subject + '</td><td><span class="status-badge ' + t
                        .status + '">' + t.status.toUpperCase() +
                        '</span></td><td><span class="status-badge ' + t.priority + '">' + t.priority
                        .toUpperCase() + '</span></td></tr>';
                }).join('');

                var totalBadge = invs.filter(function(i) { return i.status === 'unpaid' || i.status === 'overdue'; })
                    .length + tkts.filter(function(t) { return t.status === 'open'; }).length;
                document.getElementById('notifDot').textContent = totalBadge || '';
                renderBandwidthChart();
            }

            window.payCustomerInvoice = function(id) {
                var inv = invoices.find(function(i) { return i.id === id; });
                if (inv) {
                    inv.status = 'paid';
                    data.invoices = invoices;
                    if (currentCustomerName) renderCustomerAll(currentCustomerName);
                    logActivity(currentCustomerName || 'Customer', 'Paid Invoice', 'Invoice #INV-' + String(id)
                        .padStart(4, '0'));
                    showToast('Payment successful! Invoice #INV-' + String(id).padStart(4, '0') + ' paid.',
                        'success');
                    saveData();
                }
            };

            // ================================================================
            // CUSTOMER: CHANGE PACKAGE
            // ================================================================
            document.getElementById('changePackageBtn')?.addEventListener('click', function() {
                if (!currentCustomerName) { showToast('Please log in as a customer.', 'error'); return; }
                var c = getCustomerByName(currentCustomerName);
                if (!c) return;
                document.getElementById('modalTitle').textContent = 'Change Package';
                document.getElementById('modalSub').textContent = 'Select a new package for your account.';
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Current Package</label><input type="text" value="' + c
                    .package + '" disabled /></div><div class="form-group"><label>New Package</label><select id="f_new_package">' +
                    packages.map(function(p) { return '<option value="' + p.name + '" ' + (p.name === c
                        .package ? 'selected' : '') + '>' + p.name + ' ($' + p.price +
                        '/mo)</option>'; }).join('') +
                    '</select></div><div class="field-hint">Your new package will be effective immediately.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var newPkg = document.getElementById('f_new_package').value;
                    if (newPkg === c.package) { showToast('You already have this package.', 'info');
                        closeModal(); return; }
                    var idx = customers.findIndex(function(cust) { return cust.name === currentCustomerName; });
                    if (idx > -1) {
                        customers[idx].package = newPkg;
                        data.customers = customers;
                        logActivity(currentCustomerName, 'Changed Package', 'Changed from ' + c.package +
                            ' to ' + newPkg);
                        renderCustomerAll(currentCustomerName);
                        closeModal();
                        showToast('Package changed to ' + newPkg + ' successfully!', 'success');
                        saveData();
                    }
                };
            });

            // ================================================================
            // REGISTER
            // ================================================================
            registerLink.addEventListener('click', function(e) {
                e.preventDefault();
                document.getElementById('modalTitle').textContent = 'Register New Account';
                document.getElementById('modalSub').textContent = 'Create your customer account.';
                document.getElementById('modalBody').innerHTML =
                    '<div class="form-group"><label>Full Name</label><input type="text" id="reg_name" placeholder="Your name" required /></div><div class="form-group"><label>Email</label><input type="email" id="reg_email" placeholder="your@email.com" required /></div><div class="form-group"><label>Password</label><input type="password" id="reg_password" placeholder="Create a password" required /></div><div class="form-group"><label>Package</label><select id="reg_package">' +
                    packages.map(function(p) { return '<option value="' + p.name + '">' + p.name +
                        '</option>'; }).join('') +
                    '</select></div><div class="field-hint">After registration, you\'ll be logged in automatically.</div>';
                openModal();
                document.getElementById('modalConfirm').onclick = function() {
                    var name = document.getElementById('reg_name').value.trim();
                    var email = document.getElementById('reg_email').value.trim();
                    var password = document.getElementById('reg_password').value.trim();
                    var pkg = document.getElementById('reg_package').value;
                    if (!name || !email || !password) { showToast('All fields are required.', 'error');
                        return; }
                    if (customers.some(function(c) { return c.email === email; })) { showToast(
                            'This email is already registered.', 'error'); return; }
                    var newId = nextCustomerId++;
                    customers.push({ id: newId, name: name, email: email, package: pkg, status: 'active',
                        dataUsed: 0, connection: 'online', lat: 27.7172, lng: 85.3240 });
                    data.customers = customers;
                    data.nextCustomerId = nextCustomerId;
                    logActivity(name, 'Registered', 'New customer registration');
                    currentUser = 'customer';
                    currentCustomerName = name;
                    closeModal();
                    switchToCustomer(name);
                    showToast('Registration successful! Welcome, ' + name + '!', 'success');
                    saveData();
                    document.getElementById('modalConfirm').onclick = function() {};
                };
            });

            // ================================================================
            // LOGIN / LOGOUT
            // ================================================================
            function switchToAdmin() {
                loginPage.style.display = 'none';
                appContainer.style.display = 'flex';
                document.body.classList.remove('customer-mode');
                document.getElementById('roleLabel').textContent = 'Admin';
                document.getElementById('headerRole').textContent = 'Admin';
                document.getElementById('sidebarRoleBadge').innerHTML =
                '<i class="fas fa-user-shield"></i> Admin';
                document.getElementById('headerBadge').innerHTML = '<i class="fas fa-crown"></i> Admin';
                document.querySelectorAll('.page').forEach(function(p) { p.classList.remove('active'); });
                document.getElementById('page-dashboard').classList.add('active');
                document.querySelectorAll('.nav-item').forEach(function(n) { n.classList.remove('active'); });
                document.querySelector('.nav-item[data-page="dashboard"]').classList.add('active');
                document.getElementById('pageTitle').innerHTML = 'Dashboard <span>– overview</span>';
                checkAutoBilling();
                renderAdminAll();
                setTimeout(renderAdminCharts, 200);
                setTimeout(renderReportCharts, 300);
                resetSessionTimer();
            }

            function switchToCustomer(name) {
                loginPage.style.display = 'none';
                appContainer.style.display = 'flex';
                document.body.classList.add('customer-mode');
                document.getElementById('roleLabel').textContent = 'Customer';
                document.getElementById('headerRole').textContent = 'Customer';
                document.getElementById('sidebarRoleBadge').innerHTML = '<i class="fas fa-user"></i> Customer';
                document.getElementById('headerBadge').innerHTML = '<i class="fas fa-user"></i> Customer';
                document.querySelectorAll('.page').forEach(function(p) { p.classList.remove('active'); });
                document.getElementById('page-c-dashboard').classList.add('active');
                document.querySelectorAll('.nav-item').forEach(function(n) { n.classList.remove('active'); });
                document.querySelector('.nav-item[data-page="c-dashboard"]').classList.add('active');
                document.getElementById('pageTitle').innerHTML = 'My Dashboard <span>– welcome</span>';
                renderCustomerAll(name);
                resetSessionTimer();
            }

            function logout() {
                appContainer.style.display = 'none';
                loginPage.style.display = 'flex';
                currentUser = null;
                currentCustomerName = null;
                document.body.classList.remove('customer-mode');
                loginUser.value = 'admin';
                loginPass.value = 'admin';
                loginRole.value = 'admin';
                loginError.style.display = 'none';
                clearTimeout(sessionTimer);
                if (mapInstance) { mapInstance.remove();
                    mapInstance = null; }
                showToast('Signed out successfully', 'info');
            }

            // ---- LOGIN ----
            loginBtn.addEventListener('click', function() {
                var role = loginRole.value;
                var user = loginUser.value.trim();
                var pass = loginPass.value.trim();
                if (role === 'admin' && user === 'admin' && pass === 'admin') {
                    loginError.style.display = 'none';
                    currentUser = 'admin';
                    currentCustomerName = null;
                    switchToAdmin();
                    logActivity('Admin', 'Logged In', 'Admin login');
                    showToast('Welcome back, Admin!', 'success');
                    return;
                }
                if (role === 'customer' && user === 'customer' && pass === 'customer') {
                    loginError.style.display = 'none';
                    currentUser = 'customer';
                    currentCustomerName = 'Pranjal Neupane';
                    switchToCustomer(currentCustomerName);
                    logActivity('Customer', 'Logged In', 'Customer login');
                    showToast('Welcome back, Pranjal!', 'success');
                    return;
                }
                loginError.style.display = 'block';
                showToast('Invalid credentials. Please try again.', 'error');
            });
            signOutBtn.addEventListener('click', logout);
            forgotPassword.addEventListener('click', function(e) {
                e.preventDefault();
                showToast('Password reset link sent to your email (demo).', 'info');
                logActivity('System', 'Password Reset Request', 'User requested password reset');
            });
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && loginPage.style.display !== 'none') {
                    loginBtn.click();
                }
            });

            // ================================================================
            // NAVIGATION
            // ================================================================
            document.querySelectorAll('.nav-item[data-page]').forEach(function(item) {
                item.addEventListener('click', function() {
                    var page = this.dataset.page;
                    document.querySelectorAll('.nav-item').forEach(function(n) { n.classList.remove(
                        'active'); });
                    this.classList.add('active');
                    document.querySelectorAll('.page').forEach(function(p) { p.classList.remove('active'); });
                    var target = document.getElementById('page-' + page);
                    if (target) target.classList.add('active');
                    var titles = {
                        dashboard: 'Dashboard <span>– overview</span>',
                        customers: 'Customers <span>– manage subscribers</span>',
                        packages: 'Packages <span>– internet plans</span>',
                        billing: 'Billing <span>– invoices & payments</span>',
                        tickets: 'Tickets <span>– support requests</span>',
                        staff: 'Staff <span>– team management</span>',
                        'network-ops': 'Network Operations <span>– infrastructure</span>',
                        reports: 'Reports <span>– analytics & insights</span>',
                        map: 'Customer Locations <span>– geolocation</span>',
                        help: 'Help Center <span>– FAQs & support</span>',
                        activity: 'Activity Logs <span>– audit trail</span>',
                        'c-dashboard': 'My Dashboard <span>– welcome</span>',
                        'c-profile': 'My Profile <span>– account details</span>',
                        'c-payments': 'My Payments <span>– invoice history</span>',
                        'c-tickets': 'My Tickets <span>– support history</span>',
                        'c-submit': 'Submit Ticket <span>– request support</span>'
                    };
                    document.getElementById('pageTitle').innerHTML = titles[page] || 'Dashboard';
                    if (page === 'dashboard') { setTimeout(renderAdminCharts, 150);
                        setTimeout(renderReportCharts, 250); }
                    if (page === 'reports') setTimeout(renderReportCharts, 200);
                    if (page === 'network-ops') renderNetworkOps();
                    if (page === 'map') setTimeout(initMap, 300);
                    if (page.startsWith('c-') && currentCustomerName) renderCustomerAll(
                    currentCustomerName);
                    if (page === 'activity') renderActivityLogs();
                });
            });

            // ================================================================
            // MAP (Leaflet)
            // ================================================================
            function initMap() {
                var container = document.getElementById('customerMap');
                if (!container) return;
                if (mapInstance) { mapInstance.invalidateSize(); return; }
                if (typeof L === 'undefined') { setTimeout(initMap, 500); return; }
                mapInstance = L.map(container).setView([27.7172, 85.3240], 10);
                L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', { attribution: '© OpenStreetMap' })
                    .addTo(mapInstance);
                customers.forEach(function(c) {
                    if (c.lat && c.lng) {
                        var color = c.connection === 'online' ? '#10b981' : '#ef4444';
                        var status = c.connection === 'online' ? 'Online' : 'Offline';
                        L.circleMarker([c.lat, c.lng], { radius: 8, fillColor: color, color: '#fff',
                                weight: 2, fillOpacity: 0.8 }).addTo(mapInstance).bindPopup(
                            '<strong>' + c.name + '</strong><br/>Package: ' + c.package +
                            '<br/>Status: ' + status + '<br/>Data: ' + (c.dataUsed || 0).toFixed(1) +
                            ' GB');
                    }
                });
            }

            // ================================================================
            // HELP CENTER SEARCH
            // ================================================================
            document.getElementById('helpSearch')?.addEventListener('input', function() {
                var q = this.value.toLowerCase();
                document.querySelectorAll('.faq-item').forEach(function(item) {
                    var text = item.textContent.toLowerCase();
                    item.style.display = text.includes(q) ? '' : 'none';
                });
            });
            document.querySelectorAll('.faq-item .question').forEach(function(q) {
                q.addEventListener('click', function() { this.parentElement.classList.toggle('open'); });
            });

            // ================================================================
            // MODAL HELPERS
            // ================================================================
            function openModal() { document.getElementById('modalOverlay').classList.add('open'); }

            function closeModal() { document.getElementById('modalOverlay').classList.remove('open'); }
            document.getElementById('modalCancel').addEventListener('click', closeModal);
            document.getElementById('modalOverlay').addEventListener('click', function(e) { if (e.target === this)
                    closeModal(); });

            // ================================================================
            // EVENT LISTENERS (Admin buttons)
            // ================================================================
            document.getElementById('btnAddCustomer').addEventListener('click', function() { openCustomerModal(null); });
            document.getElementById('btnAddPackage').addEventListener('click', function() { openPackageModal(null); });
            document.getElementById('btnAddInvoice').addEventListener('click', function() { openInvoiceModal(null); });
            document.getElementById('btnAddTicket').addEventListener('click', function() { openTicketModal(null); });
            document.getElementById('btnAddStaff').addEventListener('click', function() { openStaffModal(null); });
            document.getElementById('customerSearch').addEventListener('input', function() { customerPage = 1;
                renderAdminCustomers(this.value, document.getElementById('filterPackage').value, document
                    .getElementById('filterStatus').value); });
            document.getElementById('filterPackage').addEventListener('change', function() { customerPage = 1;
                renderAdminCustomers(document.getElementById('customerSearch').value, this.value, document
                    .getElementById('filterStatus').value); });
            document.getElementById('filterStatus').addEventListener('change', function() { customerPage = 1;
                renderAdminCustomers(document.getElementById('customerSearch').value, document.getElementById(
                    'filterPackage').value, this.value); });

            document.getElementById('cSubmitTicketBtn').addEventListener('click', function() {
                if (!currentCustomerName) { showToast('Please log in as a customer.', 'error'); return; }
                var subject = document.getElementById('cNewTicketSubject').value.trim();
                var priority = document.getElementById('cNewTicketPriority').value;
                if (!subject) { showToast('Please enter a subject.', 'error'); return; }
                var newId = nextTicketId++;
                tickets.push({ id: newId, customer: currentCustomerName, subject: subject, status: 'open',
                    priority: priority });
                data.tickets = tickets;
                data.nextTicketId = nextTicketId;
                logActivity(currentCustomerName, 'Submitted Ticket', 'Ticket #TCK-' + String(newId).padStart(4,
                    '0') + ': ' + subject);
                document.getElementById('cNewTicketSubject').value = '';
                renderCustomerAll(currentCustomerName);
                showToast('Ticket submitted successfully!', 'success');
                saveData();
                // navigate to my tickets
                document.querySelectorAll('.nav-item').forEach(function(n) { n.classList.remove('active'); });
                document.querySelector('.nav-item[data-page="c-tickets"]').classList.add('active');
                document.querySelectorAll('.page').forEach(function(p) { p.classList.remove('active'); });
                document.getElementById('page-c-tickets').classList.add('active');
                document.getElementById('pageTitle').innerHTML = 'My Tickets <span>– support history</span>';
            });

            document.getElementById('notifToggle').addEventListener('click', function() {
                var count = document.getElementById('notifDot').textContent;
                showToast('You have ' + count + ' notifications', 'info');
            });

            // ================================================================
            // RESIZE HANDLER
            // ================================================================
            var resizeTimer;
            window.addEventListener('resize', function() {
                clearTimeout(resizeTimer);
                resizeTimer = setTimeout(function() {
                    if (document.getElementById('page-dashboard').classList.contains('active') &&
                        currentUser === 'admin') { renderAdminCharts(); }
                    if (document.getElementById('page-reports').classList.contains('active') && currentUser ===
                        'admin') { renderReportCharts(); }
                    if (mapInstance) mapInstance.invalidateSize();
                }, 250);
            });

            // ================================================================
            // INIT
            // ================================================================
            loginPage.style.display = 'flex';
            appContainer.style.display = 'none';
            document.body.classList.remove('customer-mode');
            logActivity('System', 'System Started', 'Application loaded successfully');
            checkAutoBilling();
            console.log('🚀 NetSphere Pro loaded successfully!');
            console.log('🔑 Login with: admin/admin or customer/customer');
        })();
    </script>
</body>
</html>
