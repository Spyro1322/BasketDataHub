from basketball_reference_scraper.box_scores import get_box_scores

s = get_box_scores('2020-01-13', 'CHI', 'BOS', period='GAME', stat_type='ADVANCED')
print(s)
