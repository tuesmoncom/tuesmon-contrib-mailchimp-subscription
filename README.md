Tuesmon Contrib MailChimp Subscription
====================================

Tuesmon plugin to subscribe and unsubscribe users to the newsletter in [MailChimp]("http://mailchimp.com/").


Installation
------------
### Production env

#### Tuesmon Back

In your Tuesmon back python virtualenv install the pip package `tuesmon-contrib-mailchimp-subscription` with:

```bash
  pip install -e "git+https://github.com/tuesmoncom/tuesmon-contrib-mailchimp-subscription.git@stable#egg=tuesmon-contrib-mailchimp-subscription&subdirectory=back"
```

Then modify in `tuesmon-back` your `settings/local.py` and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["tuesmon_contrib_mailchimp_subscription"]
```


#### Tuesmon Front

Download in your `dist/plugins/` directory of Tuesmon front the `tuesmon-contrib-mailchimp-subscription` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/tuesmoncom/tuesmon-contrib-mailchimp-subscription/branches/stable/front/dist" "mailchimp-subscription"
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailchimp-subscription/mailchimp-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailchimp-subscription/mailchimp-subscription.json"
    ]
...
```

### Dev env

#### Tuesmon Back

Clone the repo and

```bash
  cd tuesmon-contrib-mailchimp-subscription/back
  workon tuesmon
  pip install -e .
```

Then modify in `tuesmon-back` your `settings/local.py` and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["tuesmon_contrib_mailchimp_subscription"]
```

#### Tuesmon Front

After clone the repo link `dist` in `tuesmon-front` plugins directory:

```bash
  cd tuesmon-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../tuesmon-contrib-mailchimp-subscription/front/dist mailchimp-subscription
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailchimp-subscription/mailchimp-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailchimp-subscription/mailchimp-subscription.json"
    ]
...
```

In the plugin source dir `tuesmon-contrib-mailchimp-subscription` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.


Tests
-----
```bash
  cd tuesmon-back
  workon tuesmon
  py.test ../tuesmon-contrib-mailchimp-subscription/back/tuesmon_contrib_mailchimp_subscription_tests
```
