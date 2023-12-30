from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import paramiko

class SSHButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Replace 'your_ssh_command' with the actual SSH command you want to execute
        ssh_command = "ls"

        # Function to execute SSH command
        def execute_ssh_command(instance):
            try:
                # SSH connection parameters
                ssh_host = '10.0.0.5'
                ssh_port = 22
                ssh_username = 'dietpi'
                ssh_password = '82653333'

                # Create SSH client
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # Connect to the SSH server
                ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

                # Execute the SSH command
                stdin, stdout, stderr = ssh_client.exec_command(ssh_command)
                result = stdout.read().decode('utf-8')

                # Print the result or handle it as needed
                print(result)

                # Close te SSH connection
                ssh_client.close()
            except Exception as e:
                print(f"Error executing SSH command: {e}")

        # Create the button
        ssh_button = Button(text='Send SSH Command', on_press=execute_ssh_command)

        # Add the button to the layout
        layout.add_widget(ssh_button)

        return layout

if __name__ == '__main__':
    SSHButtonApp()