#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Print/export all e-mail addresses from a MailChimp list.

Copyright (c) 2017 K Kollmann <code∆k.kollmann·moe>

The program reads a MailChimp subscribers list exported to .csv format,
filters out the column containing e-mail addresses, and
- prints all e-mail addresses to stdout and
- writes them to a .txt file.

By default, the e-mail addresses get sorted alphabetically,
though users can choose to suppress sorting as well as
printing to stdout or writing the addresses to a file.

If the column containing the e-mail addresses does not
use MailChimp's default header "Email Address", users can
provide an alternative header.

They can also provide the path to a different file name
for saving the addresses. By default, they get saved to a
file named "emails_from_mailchimp.txt".
"""

import csv
from log import log


def extract_emails(fname, email='Email Address',
                   outfile="emails_from_mailchimp.txt",
                   nofile=False, nolog=False, sort=True):
    """
    Extract e-mail addresses from a CSV-exported MailChimp list.

    :param fname: the input .csv file
    :param email: the header of the column containing all e-mail addresses
    :param outfile: the .txt file the addresses will get written to
    :param nofile: suppresses the creation of a text file if set to True
    :param nolog: suppresses logging the addresses to stdout if set to True
    :param sort: sorts e-mail addresses alphabetically if set to True

    :return a list containing all e-mail addresses
    """
    addresses = []
    try:
        with open(fname, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            next(reader)
            for item in reader:
                try:
                    addresses.append(item[email])
                except KeyError:
                    log.error("The provided CSV file does not contain "
                              "the header \"{}\".\n"
                              "Please provide the correct header name "
                              "for the column containing e-mail "
                              "addresses.".format(email))
                    return
    except FileNotFoundError:
        log.error("The input file is not available. "
                  "Please provide a valid path.")
    except IsADirectoryError:
        log.error("The input file is not a CSV file but a directory.")
    except StopIteration:
        log.error("The input file cannot be read. "
                  "Please provide a valid CSV file.")

    if sort:
        addresses.sort()

    if not nolog:
        for address in addresses:
            log.info(address)

    if not nofile:
        try:
            with open(outfile, 'w') as txtfile:
                for address in addresses:
                    txtfile.write(address + '\n')
        except FileNotFoundError:
            log.error("The file you are trying to write to "
                      "does not exist.")
        except PermissionError:
            log.error("You do not have permission to write to the file "
                      "whose path you provided.")

    return addresses


def main():
    """Main function."""

    # ---USER INPUT---
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="")
    parser.add_argument('-f', '--file',
                        help="CSV file to read MailChimp "
                             "list subscriber addresses from.")
    parser.add_argument('-e', '--email',
                        default='Email Address',
                        help="Submit an alternative value for the header "
                             "of the column\n"
                             "containing e-mail addresses. "
                             "Defaults to %(default)s.")
    parser.add_argument('-o', '--outfile',
                        default='emails_from_mailchimp.txt',
                        help="Provide a name/path for a text file which "
                             "all addresses\n"
                             "should get written to. "
                             "Defaults to %(default)s.")
    parser.add_argument('-n', '--nofile', action='store_true',
                        help="Suppress creation of a .txt file.\n")
    parser.add_argument('-l', '--nolog', action='store_true',
                        help="Suppress logging of addresses to stdout.\n")
    parser.add_argument('-s', '--nosort', action='store_false',
                        help="Suppress alphabetical sorting of addresses.\n")
    args = parser.parse_args()

    email = args.email
    outfile = args.outfile
    nofile = args.nofile
    nolog = args.nolog
    sort = args.nosort

    if args.file:
        fname = args.file
    else:
        log.warning("No input file provided!")
        try:
            fname = input("Path to CSV export of a MailChimp list: ")
        except KeyboardInterrupt:
            sys.exit("\nProgram aborted by user.")

    extract_emails(fname, email=email, outfile=outfile,
                   nofile=nofile, nolog=nolog, sort=sort)


if __name__ == "__main__":
    import argparse
    import sys

    main()
