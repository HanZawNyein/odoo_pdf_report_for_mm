{
    "name": "Reporter",
    "author": "Han Zaw Nyein",
    "license": "LGPL-3",
    "depends": [],
    "data": [
        'security/ir.model.access.csv',

        'views/hz_reporter.xml',
        'report/hz_reporter.xml',
        'report/report.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'hz_reporter/static/src/**/*',
        ]
    }
}
