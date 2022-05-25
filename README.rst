Joomla 4 - Mobile-ready user-friendly content management
========================================================

`Joomla!`_ is an award-winning Content Management System (CMS) for
building websites as well as a Model-view-controller (MVC) Web
Application Development framework. Features include page caching to
improve performance, RSS feeds, printable versions of pages, news
flashes, blogs, polls, website searching, and language
internationalization.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Joomla 4 configurations:
   
   - Installed from upstream source code to /var/www/joomla

   - Includes `Joomla Console`_

   **Security note**: Updates to Joomla may require supervision so
   they **ARE NOT** configured to install automatically. See `Joomla
   documentation`_ for upgrading.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

We recommend subscribing to the `Joomla Security Feed`_ (RSS/mailing list)

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**
-  Joomla: username **admin**


.. _Joomla!: https://www.joomla.org/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: https://www.adminer.org
.. _Joomla documentation: https://docs.joomla.org/J4.x:Updating_from_an_existing_version
.. _Joomla Security Feed: http://feeds.joomla.org/JoomlaSecurityNews
.. _Joomla Console: https://github.com/joomlatools/joomlatools-console
