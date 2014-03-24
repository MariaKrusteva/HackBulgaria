def slope_style_score(scores):
	scores.remove(max(scores))
	scores.remove(min(scores))
	return round(sum(scores)/len(scores),2)