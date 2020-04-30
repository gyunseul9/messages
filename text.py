class Text:

  def get_text(choose):

    text = {
        'slack':'슬랙 메시지',
        'teams':'팀즈 메시지',
        'telegram':'텔레그램 메시지'
    }       

    if(choose == 'slack'):
      value = text.get('slack')
    elif(choose == 'teams'):
      value = text.get('teams')  
    elif(choose == 'telegram'):
      value = text.get('telegram')       
    else:
      print('Not Selected')
      value = ''

    return value