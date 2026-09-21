# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yuito <yuito@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/22 01:01:18 by yuito             #+#    #+#              #
#    Updated: 2026/09/22 02:44:00 by yuito            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	display_name = seed_type.capitalize()
	if unit == "packets":
		print(f"{display_name} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{display_name} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{display_name} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
