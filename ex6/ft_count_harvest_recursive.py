# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yuito <yuito@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 00:31:04 by yuito             #+#    #+#              #
#    Updated: 2026/09/22 00:58:48 by yuito            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))

	def count(day):
		if day > days:
			return

		print(f"Day {day}")
		count(day + 1)

	count(1)
	print("Harvest time!")
