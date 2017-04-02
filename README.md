# MailChimp Mail 2 TXT

Extract e-mail addresses from a CSV export of a MailChimp list and print them to `stdout` / save them to a .txt file.

## Background
Wanting to switch from [MailChimp](https://mailchimp.com/) to [Mailman](https://www.gnu.org/software/mailman/) to reduce bulk/work when sending out updates over a news list, I was looking for a way to easily export e-mail addresses collected via MailChimp and reimport them into Mailman.

MailChimp subscriber lists can be exported as `.csv` files; Mailman accepts lists of (or files containing) e-mail addresses with each address on its own line.

## Requirements
While it might work with other Python versions just fine, the script was only tested with Python 3.5.

Before running the script, rename `logconf.json.template` to `logconf.json` (and adapt it to your needs if necessary).

## Usage
You can either `import` the module's `extract_emails` function into other scripts or run the file as standalone script.

The module/script expects at least an input file (the .csv export of your MailChimp list). When running it directly, use the `-f` flag to provide the path for the input file:

```
$ python mailchimpmail2txt.py -f MAILCHIMPEXPORT.csv
```

You can also set an **alternative header** for the column containing the e-mail addresses (by default, MailChimp uses "Email Address"), an **alternative** file name/path for the **output file**, or **suppress writing to a file** – or the standard output – altogether. By default, the e-mail addresses get sorted alphabetically, though you can also suppress that.

Use `--help` to learn how to run the script with these additional options:

```
$ python mailchimpmail2txt.py --help
```

## Licence
This script is released under an MIT licence; see the [LICENSE](LICENSE) file for terms & conditions.

<br>
<span xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">This README was created using <span rel="dct:type" href="http://purl.org/dc/dcmitype/Text"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/keikoro/README.template">README.template</a> by <span property="cc:attributionName">K Kollmann</span>, which is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</span>
