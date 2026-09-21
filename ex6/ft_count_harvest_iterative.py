# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yuito <yuito@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 00:30:58 by yuito             #+#    #+#              #
#    Updated: 2026/09/22 00:43:27 by yuito            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for day in range(1, days + 1):
		print(f"Day {day}")
	print("Harvest time!")
