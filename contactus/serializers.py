from rest_framework import serializers, status
from .models import contactus, subscribe
from django.core.mail import send_mail, send_mass_mail


class contactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactus
        fields = '__all__'

    def create(self, validate_data):
        instance = super(contactusSerializer, self).create(validate_data)

        user_name = validate_data.get('name')
        user_email = validate_data.get('email')
        user_subject = validate_data.get('subject')
        user_message = validate_data.get('message')

        # USER MAIL FORMATE START
        user_email_subject = "Thinkahoy: Thank You for contacting us"
        user_email_message = "We appreciate Mr/Miss.{} you contacting Thinkahoy. One of our colleagues will get back in touch with you soon! Have a great day! ".format(
            user_name)
        # USER MAIL FORMATE END

        # THINKAHOY MAIL FORMATE START
        Thinkahoy_email_subject = "Thinkahoy: Mr {} is subminted contact us form".format(
            user_name)
        Thinkahoy_message = """
            some demo text ....
            From: {} \n
            Email: {} \n
            Subject: {} \n
            Message: {}""".format(user_name, user_email, user_subject, user_message)
        # THINKAHOY MAIL FORMATE END

        user_mail_formate = (
            user_email_subject,
            user_email_message,
            'noreply@thinkahoy.com',
            [user_email]
        )

        thinkahoy_mail_copy = (
            Thinkahoy_email_subject,
            Thinkahoy_message,
            'noreply@thinkahoy.com',
            ['contact@thinkahoy.com']
        )

        send_mass_mail((user_mail_formate, thinkahoy_mail_copy),
                       fail_silently=False)
        return instance


class subscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscribe
        fields = '__all__'
