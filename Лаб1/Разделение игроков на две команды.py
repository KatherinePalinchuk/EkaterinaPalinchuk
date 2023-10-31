list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

separ_index = len(list_players) // 2
team_1 = list_players[:separ_index]
team_2 = list_players[separ_index:]
print(team_1)
print(team_2)
