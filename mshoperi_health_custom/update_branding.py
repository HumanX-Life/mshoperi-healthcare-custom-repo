import os
import sys

import frappe


def update_branding():
    # Initialize Frappe if not already initialized (e.g. when run as module)
    try:
        frappe.local.site
    except AttributeError:
        site = os.environ.get("SITE_NAME", "mshoperi-health.local")
        sites_path = "/home/frappe/frappe-bench/sites"
        os.chdir(sites_path)
        frappe.init(site, sites_path=sites_path)
        frappe.connect()

    # Update System Settings
    frappe.db.set_value("System Settings", None, "app_name", "Mshoperi Health")
    if not frappe.db.get_value("System Settings", None, "language"):
        frappe.db.set_value("System Settings", None, "language", "en")
    if not frappe.db.get_value("System Settings", None, "time_zone"):
        frappe.db.set_value("System Settings", None, "time_zone", "Africa/Harare")
    if not frappe.db.get_value("System Settings", None, "country"):
        frappe.db.set_value("System Settings", None, "country", "Zimbabwe")

    # Update Website Settings
    frappe.db.set_value("Website Settings", None, "app_name", "Mshoperi Health")
    frappe.db.set_value("Website Settings", None, "app_logo", "/assets/mshoperi_health_custom/images/logo.png")
    frappe.db.set_value("Website Settings", None, "brand_html", '<div><img src="/assets/mshoperi_health_custom/images/logo.png" style="max-width: 150px;"/></div>')
    frappe.db.set_value("Website Settings", None, "copyright", "Mshoperi Health")

    frappe.db.commit()
    print("Branding updated successfully")


if __name__ == "__main__":
    update_branding()
