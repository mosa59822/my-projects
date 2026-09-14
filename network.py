import tkinter as tk
from tkinter import ttk, messagebox
import threading
import socket
import psutil
import time

from network_scanner import (
    get_local_ip,
    get_gateway,
    scan_network
)


class NetworkMonitor:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Network Monitor - Python"
        )

        self.root.geometry(
            "1100x650"
        )

        self.root.minsize(
            900,
            550
        )

        self.scanning = False

        self.setup_style()

        self.create_header()

        self.create_info_panel()

        self.create_controls()

        self.create_table()

        self.create_statusbar()

        self.update_network_info()

    # ----------------------------------
    # Style
    # ----------------------------------

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            rowheight=32,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

        style.configure(
            "Title.TLabel",
            font=(
                "Segoe UI",
                20,
                "bold"
            )
        )

        style.configure(
            "Info.TLabel",
            font=(
                "Segoe UI",
                11
            )
        )

        style.configure(
            "Scan.TButton",
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            padding=10
        )

    # ----------------------------------
    # Header
    # ----------------------------------

    def create_header(self):

        frame = ttk.Frame(
            self.root,
            padding=15
        )

        frame.pack(
            fill="x"
        )

        title = ttk.Label(
            frame,
            text="🌐 Network Monitor",
            style="Title.TLabel"
        )

        title.pack(
            side="left"
        )

        self.connection_label = ttk.Label(
            frame,
            text="● Checking...",
            font=(
                "Segoe UI",
                11,
                "bold"
            )
        )

        self.connection_label.pack(
            side="right"
        )

    # ----------------------------------
    # Information
    # ----------------------------------

    def create_info_panel(self):

        frame = ttk.LabelFrame(
            self.root,
            text=" Network Information ",
            padding=12
        )

        frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.ip_label = ttk.Label(
            frame,
            text="Local IP: ---",
            style="Info.TLabel"
        )

        self.ip_label.grid(
            row=0,
            column=0,
            padx=20,
            sticky="w"
        )

        self.gateway_label = ttk.Label(
            frame,
            text="Gateway: ---",
            style="Info.TLabel"
        )

        self.gateway_label.grid(
            row=0,
            column=1,
            padx=20,
            sticky="w"
        )

        self.interface_label = ttk.Label(
            frame,
            text="Interface: ---",
            style="Info.TLabel"
        )

        self.interface_label.grid(
            row=0,
            column=2,
            padx=20,
            sticky="w"
        )

    # ----------------------------------
    # Controls
    # ----------------------------------

    def create_controls(self):

        frame = ttk.Frame(
            self.root,
            padding=(15, 10)
        )

        frame.pack(
            fill="x"
        )

        ttk.Label(
            frame,
            text="Network:"
        ).pack(
            side="left"
        )

        self.network_entry = ttk.Entry(
            frame,
            width=25
        )

        self.network_entry.pack(
            side="left",
            padx=8
        )

        local_ip = get_local_ip()

        if local_ip != "Unknown":

            parts = local_ip.split(".")

            network = (
                f"{parts[0]}."
                f"{parts[1]}."
                f"{parts[2]}.0/24"
            )

            self.network_entry.insert(
                0,
                network
            )

        self.scan_button = ttk.Button(
            frame,
            text="🔍 Scan Network",
            style="Scan.TButton",
            command=self.start_scan
        )

        self.scan_button.pack(
            side="left",
            padx=10
        )

        self.refresh_button = ttk.Button(
            frame,
            text="⟳ Refresh",
            command=self.update_network_info
        )

        self.refresh_button.pack(
            side="left"
        )

        self.progress = ttk.Progressbar(
            frame,
            mode="indeterminate",
            length=180
        )

        self.progress.pack(
            side="right"
        )

    # ----------------------------------
    # Table
    # ----------------------------------

    def create_table(self):

        frame = ttk.Frame(
            self.root,
            padding=(15, 5)
        )

        frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "ip",
            "mac",
            "hostname",
            "status",
            "ping"
        )

        self.tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "ip",
            text="IP Address"
        )

        self.tree.heading(
            "mac",
            text="MAC Address"
        )

        self.tree.heading(
            "hostname",
            text="Hostname"
        )

        self.tree.heading(
            "status",
            text="Status"
        )

        self.tree.heading(
            "ping",
            text="Ping"
        )

        self.tree.column(
            "ip",
            width=150
        )

        self.tree.column(
            "mac",
            width=180
        )

        self.tree.column(
            "hostname",
            width=250
        )

        self.tree.column(
            "status",
            width=120
        )

        self.tree.column(
            "ping",
            width=100
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # ----------------------------------
    # Status Bar
    # ----------------------------------

    def create_statusbar(self):

        self.status_label = ttk.Label(
            self.root,
            text="Ready",
            relief="sunken",
            anchor="w",
            padding=6
        )

        self.status_label.pack(
            fill="x",
            side="bottom"
        )

    # ----------------------------------
    # Network Information
    # ----------------------------------

    def update_network_info(self):

        ip = get_local_ip()

        gateway = get_gateway()

        self.ip_label.config(
            text=f"Local IP: {ip}"
        )

        self.gateway_label.config(
            text=f"Gateway: {gateway}"
        )

        interface = self.get_interface()

        self.interface_label.config(
            text=f"Interface: {interface}"
        )

        self.check_internet()

    # ----------------------------------
    # Interface
    # ----------------------------------

    def get_interface(self):

        try:

            stats = psutil.net_if_stats()

            for name, data in stats.items():

                if data.isup:

                    return name

        except:
            pass

        return "Unknown"

    # ----------------------------------
    # Internet Check
    # ----------------------------------

    def check_internet(self):

        def test():

            try:

                socket.create_connection(
                    ("8.8.8.8", 53),
                    timeout=2
                )

                self.root.after(
                    0,
                    lambda:
                    self.connection_label.config(
                        text="● Internet Online"
                    )
                )

            except:

                self.root.after(
                    0,
                    lambda:
                    self.connection_label.config(
                        text="● Internet Offline"
                    )
                )

        threading.Thread(
            target=test,
            daemon=True
        ).start()

    # ----------------------------------
    # Start Scan
    # ----------------------------------

    def start_scan(self):

        if self.scanning:
            return

        network = self.network_entry.get().strip()

        if not network:

            messagebox.showwarning(
                "Warning",
                "Enter network address."
            )

            return

        # حذف اطلاعات قبلی
        for item in self.tree.get_children():

            self.tree.delete(item)

        self.scanning = True

        self.scan_button.config(
            state="disabled"
        )

        self.progress.start(10)

        self.status_label.config(
            text=f"Scanning {network} ..."
        )

        thread = threading.Thread(
            target=self.perform_scan,
            args=(network,),
            daemon=True
        )

        thread.start()

    # ----------------------------------
    # Scan
    # ----------------------------------

    def perform_scan(self, network):

        start = time.time()

        try:

            devices = scan_network(
                network
            )

            elapsed = time.time() - start

            self.root.after(
                0,
                lambda:
                self.show_results(
                    devices,
                    elapsed
                )
            )

        except Exception as e:

            self.root.after(
                0,
                lambda:
                self.scan_error(str(e))
            )

    # ----------------------------------
    # Show Results
    # ----------------------------------

    def show_results(
        self,
        devices,
        elapsed
    ):

        self.progress.stop()

        self.scan_button.config(
            state="normal"
        )

        self.scanning = False

        for device in devices:

            ping = device["ping"]

            if ping is None:
                ping_text = "Timeout"

            else:
                ping_text = f"{ping:.1f} ms"

            self.tree.insert(
                "",
                "end",
                values=(
                    device["ip"],
                    device["mac"],
                    device["hostname"],
                    device["status"],
                    ping_text
                )
            )

        self.status_label.config(
            text=(
                f"Scan completed | "
                f"{len(devices)} device(s) found | "
                f"{elapsed:.2f} seconds"
            )
        )

    # ----------------------------------
    # Error
    # ----------------------------------

    def scan_error(self, error):

        self.progress.stop()

        self.scan_button.config(
            state="normal"
        )

        self.scanning = False

        self.status_label.config(
            text="Scan failed"

        )

        messagebox.showerror(
            "Scan Error",
            error
        )


# --------------------------------------
# Application
# --------------------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = NetworkMonitor(
        root
    )

    root.mainloop()