dia_inicio = input().split()
hora_ini, min_ini, seg_ini = list(map(int, input().split(' :')))
dia_fim = input().split()
hora_fim, min_fim, seg_fim = list(map(int, input().split(' :')))

count_passed_second = (hora_ini*60*60)+(min_ini*60)+seg_ini
count_remain_second1 = (86400-count_passed_second)
count_remain_second2 = (hora_fim*60*60)+(min_fim*60)+seg_fim
date = (int(dia_fim[-1])-1)-int(dia_inicio[-1])
count_date_second = date*86400
total_second = count_remain_second1+count_remain_second2+count_date_second


D = total_second/86400
total_second = total_second%86400
H = total_second/3600
total_second = total_second%3600
M = total_second/60
total_second = total_second%60
S = total_second


print(f'{int(D)} dia(s)')
print(f'{int(H)} hora(s)')
print(f'{int(M)} minuto(s)')
print(f'{int(S)} segundo(s)')