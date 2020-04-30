class Configuration:

  def get_token(choose):

    slack = {
        'SLACK_GROUP':['CHANNEL_NAME','WEBHOOK_TOKEN'],
    }    

    telegram = {
        'BOT_NAME':['BOT_TOKEN'],
    } 

    teams = {
        'CHANNEL_NAME':['https://schema.org/extensions','WEBHOOK_URL'],
    }    

    if(choose == 'slack'):
      value = slack.get('SLACK_GROUP')
    elif(choose == 'telegram'):
      value = telegram.get('BOT_NAME')
    elif(choose == 'teams'):
      value = teams.get('CHANNEL_NAME')       
    else:
      print('Not Selected')
      value = ''

    return value

  def get_user(choose):

    BOT_NAME = {
        'CHAT_NUMER':'MEMBER_NAME',
        'CHAT_NUMER':'MEMBER_NAME',
        'CHAT_NUMER':'MEMBER_NAME'
    } 

    if(choose == 'BOT_NAME'):
      value = BOT_NAME  
    else:
      print('Not Selected')
      value = ''

    return value

  