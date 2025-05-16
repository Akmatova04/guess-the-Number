from django.shortcuts import render
import random

def guess_number_view(request):
    # Сессиядан жашыруун санды жана аракеттердин санын алууга аракет кылуу
    secret_number = request.session.get('secret_number')
    attempts = request.session.get('attempts', 0)
    message = ""
    game_over = False

    if secret_number is None:
        # Эгер оюн жаңыдан башталса, жаңы жашыруун санды генерациялоо
        secret_number = random.randint(1, 100)
        request.session['secret_number'] = secret_number
        request.session['attempts'] = 0
        attempts = 0
        message = "1ден 100гө чейинки санды ойлодум. Таап көрүңүз!"
    
    if request.method == 'POST':
        try:
            guessed_number = int(request.POST.get('guessed_number'))
            attempts += 1
            request.session['attempts'] = attempts

            if guessed_number < secret_number:
                message = f"Сиздин сан ({guessed_number}) кичине. Дагы аракет кылыңыз."
            elif guessed_number > secret_number:
                message = f"Сиздин сан ({guessed_number}) чоң. Дагы аракет кылыңыз."
            else:
                message = f"Куттуктайм! Сиз {secret_number} санын {attempts} аракетте таптыңыз!"
                game_over = True
                # Оюн бүткөндөн кийин сессияны тазалоо (кийинки оюн үчүн)
                # же жаңы оюнду баштоону сунуштоо
                request.session.pop('secret_number', None)
                request.session.pop('attempts', None)
        except (ValueError, TypeError):
            message = "Сураныч, туура сан киргизиңиз."

    context = {
        'message': message,
        'attempts': attempts,
        'game_over': game_over,
    }
    return render(request, 'game/guess_template.html', context)

def new_game_view(request):
    # Жаңы оюн баштоо үчүн сессияны тазалоо
    if 'secret_number' in request.session:
        request.session.pop('secret_number', None)
    if 'attempts' in request.session:
        request.session.pop('attempts', None)
    # Оюн барагына кайра багыттоо (бул жерде жашыруун сан кайра генерацияланат)
    from django.shortcuts import redirect
    return redirect('guess_number_url') # Бул URLды кийин түзөбүз