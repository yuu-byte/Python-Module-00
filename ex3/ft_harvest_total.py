# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yuito <yuito@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/21 21:30:15 by yuito             #+#    #+#              #
#    Updated: 2026/09/21 21:34:15 by yuito            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day1_harvest = int(input("Day 1 harvest: "))
	day2_harvest = int(input("Day 2 harvest: "))
	day3_harvest = int(input("Day 3 harvest: "))
	total_harvest = day1_harvest + day2_harvest + day3_harvest
	print("Total harvest:", total_harvest)
