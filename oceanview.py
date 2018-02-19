"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import server.server as backend


def main():
    """
    main function for the program
    :return: None
    """
    backend.start_server('127.0.0.1', 80)


if __name__ == "__main__":
    main()