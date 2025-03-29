from django.shortcuts import render

@api_view(['POST'])
def create_notification(recipient, actor, verb, target):
    Notification.objects.create(recipient=recipient, actor=actor, verb=verb, target=target)
