#!/usr/bin/env python3
"""
Health check endpoint for Render deployment
This ensures the service stays alive and can be monitored
"""

import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "service": "AnonXMusic Bot"}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def start_health_server():
    """Start a simple HTTP server for health checks"""
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    print(f"Health check server started on port {port}")
    server.serve_forever()

def run_health_check():
    """Run health check server in background"""
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()

if __name__ == "__main__":
    # This can be used as a standalone health check service
    start_health_server()
