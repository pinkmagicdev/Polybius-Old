"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/evennia/muddev/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Polybius"

# Server ports. If enabled and marked as "visible", the port
# should be visible to the outside world on a production server.
# Note that there are many more options available beyond these.

# Telnet ports. Visible.
TELNET_ENABLED = True
TELNET_PORTS = [4000]
# (proxy, internal). Only proxy should be visible.
WEBSERVER_ENABLED = True
WEBSERVER_PORTS = [(80, 4002)]
# Telnet+SSL ports, for supporting clients. Visible.
SSL_ENABLED = False
SSL_PORTS = [4003]
# SSH client ports. Requires crypto lib. Visible.
SSH_ENABLED = False
SSH_PORTS = [4004]
# Websocket-client port. Visible.
WEBSOCKET_CLIENT_ENABLED = True
WEBSOCKET_CLIENT_PORT = 4005
# Internal Server-Portal port. Not visible.
AMP_PORT = 4006
SERVER_SESSION_CLASS = 'evennia.contrib.security.auditing.server.AuditedServerSession'
INSTALLED_APPS += (
        'django.contrib.humanize',
        'django_nyt',
        'mptt',        
        'sorl.thumbnail',
        'wiki',
        'wiki.plugins.attachments',
        'wiki.plugins.notifications',
        'wiki.plugins.images',
        'wiki.plugins.macros',
)

SITE_ID = 1

# Disable creating new accounts from the wiki
WIKI_ACCOUNT_HANDLING = False
WIKI_ACCOUNT_SIGNUP_ALLOWED = False

TEMPLATES[0]['OPTIONS']['context_processors'] += ['sekizai.context_processors.sekizai']
######################################################################
# Contrib config
######################################################################

GAME_INDEX_LISTING = {
    'game_status': 'pre-alpha',
    # Optional, comment out or remove if N/A
    'game_website': 'http://www.swagsociety.me',
    'short_description': 'Twitch based fantasy MUD, with a in game cryptocurrency.',
    # Optional but highly recommended. Markdown is supported.
    'long_description': (
        "Hello, there. You silly person.\n\n"
        "This is the start of a new paragraph. Markdown is cool. Isn't this "
        "[neat](http://evennia.com)? My game is best game. Woohoo!\n\n"
        "Time to wrap this up. One final paragraph for the road."
    ),
    'listing_contact': 'swagunclesam@gmail.com',
    # At minimum, specify this or the web_client_url options. Both is fine, too.
    'telnet_hostname': 'swagsociety.me',
    'telnet_port': 4000,
    # At minimum, specify this or the telnet_* options. Both is fine, too.
    'web_client_url': 'http://www.swagsociety.me/webclient',
}


######################################################################
# External Channel connections
######################################################################

# Note: You do *not* have to make your MUD open to
# the public to use the external connections, they
# operate as long as you have an internet connection,
# just like stand-alone chat clients. IRC requires
# that you have twisted.words installed.

# Evennia can connect to external IRC channels and
# echo what is said on the channel to IRC and vice
# versa. Obs - make sure the IRC network allows bots.
# When enabled, command @irc2chan will be available in-game
IRC_ENABLED = True

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
