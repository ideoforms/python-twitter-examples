# Python Twitter Examples

A set of Python scripts to demonstrate interactions with the Twitter API
via the [Python Twitter Tools](https://github.com/ideoforms/python-twitter-examples) module.

## Usage

These examples require Python 3. To install prerequisites:

    pip install -r requirements.txt

You will need to authenticate with Twitter to use these scripts. To do
so, sign up for developer credentials:

[https://apps.twitter.com/](https://apps.twitter.com/)

You can create access credentials directly through Twitter's web
interface, authorized under the username you used to create the app.

If you want your application to act on behalf of other users (for example,
to post on behalf of several usernames), you'll need to authorize each
separately. To be guided through this process, run:

    python twitter-authorize.py

Then add your consumer and access tokens to `config.py`.

## History

This collection was first developed for a 2012 laboratory in social data
mining for the MA/MSc Digital Sociology, Digital Journalism and Creating Social
Media courses at the Centre for Creative and Social Technology, Goldsmiths,
University of London.

    Daniel Jones <d.jones@gold.ac.uk>
    http://www.erase.net

------------------------------------------------------------------------
