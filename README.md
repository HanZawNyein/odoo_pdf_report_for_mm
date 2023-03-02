### Report.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <record id="action_hz_reporter_report" model="ir.actions.report">
        <field name="name">Reporter PDF</field>
        <field name="model">hz.reporter</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">hz_reporter.hz_reporter_template</field>
        <field name="report_file">hz_reporter.hz_reporter_template</field>
        <field name="binding_model_id" ref="model_hz_reporter"/>
        <field name="binding_type">report</field>
    </record>
</odoo>
```

### hz_reporter.xml
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <template id="hz_reporter_template">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="o">
                <t t-call="web.external_layout">
                    <div class="page">
                        <h1>Odoo တွင် PDF ကို မြန်မာစာရအောင် ရေးနည်း</h1>
                        <h2>Report title</h2>
                        <p>This object's name is
                            <span t-field="o.name"/>
                        </p>
                        <hr/>
                        <p t-out="o.description"/>
                        <p t-field="o.description"/>
                    </div>
                </t>
            </t>
        </t>
    </template>
</odoo>
```