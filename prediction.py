from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField

class PredictionForm(FlaskForm):
    SFH = SelectField("SFH",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")],validate_choice=True)
    POPUP_WINDOW= SelectField("POPUP_WINDOW",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    SSL = SelectField("SSL",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    REQUEST_URL = SelectField("REQUEST_URL",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    URL_OF_ANCHOR = SelectField("URL_OF_ANCHOR",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    WEB_TRAFFIC = SelectField("WEB_TRAFFIC",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    URL_LENGTH = SelectField("URL_LENGTH",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS"),(-1,"PHISHING")])
    AGE_OF_DOMAIN= SelectField("AGE_OF_DOMAIN",choices=[(1,"LEGITIMATE"),(-1,"PHISHING")])
    HAVING_IP_ADDRESS= SelectField("HAVING_IP_ADDRESS",choices=[(1,"LEGITIMATE"),(0,"SUSPICIOUS")])
    SUBMIT = SubmitField("SUBMIT")
