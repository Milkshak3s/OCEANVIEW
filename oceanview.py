"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import server.server as backend
import frontend.frontend as frontend


def main():
    """
    main function for the program
    :return: None
    """
    backend.start_server('127.0.0.1', 80)
    frontend.kickit('127.0.0.1',81)


if __name__ == "__main__":
    main()
