# Data Mining   

This repository is the first part of a light data analysis. In this repo, I demonstrate how I collected the data I'll be using in the ‘osu_data_visualizations’ repo. This basically boils down to using python to use the site's old API service found [here](https://github.com/ppy/osu-api/wiki).  

## Requirements 

- Python 3.x   

- An Osu! account 

- An [API key](https://osu.ppy.sh/forum/ucp.php?mode=login). 

- General knowledge of how the game funcitons. 

## Description of tables  

Datasets `user.csv`, `user2.csv`, and `user3.csv` has the same column structure. Likewise, datasets `best_played.csv`, `best_played2.csv`, and `best_played3.csv` have the same structure. They should be thought of as a continuous dataset. They were broken up into parts for the sake of not have just one large dataset.   

For the `usersX.csv` files:

 | Column         | Description                                                                          | Notes                                                                               |
|----------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| user_id        | A player's  unique ID                                                                | Attached to the account. Independent of player's name.                              |
| username       | The player's current gamer tag                                                       | Could change.                                                                       |
| join_date      | The time the account was created.                                                    |                                                                                     |
| count300       | The number of times a user has clicked a circle 'accurately'                         | Margin of error is based on specific beatmap.                                       |
| count100       | The number of times a user has clicked a circle 'almost accurately'                  | Margin of error is based on specific beatmap.                                       |
| count50        | The number of times a user has clicked a circle 'just barely in time'                | Margin of error is based on specific beatmap.                                       |
| playcount      | The number of times a user has played a map.                                         | If the user was online.                                                             |
| ranked_score   | The total sum of all best score/performance for every map every played.              | Scores that were achieved online. Also, not all beatmaps are playable for rankings. |
| total_score    | The total sum of all top scores for every map regardless if they were ranked or not. |                                                                                     |
| pp_rank        | The user's global rank.                                                              | Based on overall performance.                                                       |
| accuracy       | The average accuracy for every (best played) performance.                            |                                                                                     |
| count_rank_ss  | The number of `SS` rated performances.                                               | You can only get one performance rating per map.                                    |
| count_rank_ssh | The number of silver `SS` rated performances.                                        | You can only get one performance rating per map. These are achieved with map modifiers. |
| count_rank_s         | The number of `S` rated performances.        | You can only get one performance rating per map.                                        |
| count_rank_sh        | The number of silver `S` rated performances. | You can only get one performance rating per map. These are achieved with map modifiers. |
| count_rank_a         | The number of `A` rated performances.        | You can only get one performance rating per map.                                        |
| country              | The country the user is from.                | Could change.                                                                           |
| total_seconds_played | The total time the user has played online.   |                                                                                         |
| pp_country_rank      | The user's rank relative to their country.   | Also based on overall performance.                                                      |

Map ratings are generally based on accuracy and the number of misses. I believe 95% accuracy with no misses gives a player an `S` rating.

The performance points gained from a paritcular beatmap is based on a closed function. It can be described [here](https://osu.ppy.sh/help/wiki/Performance_Points).

For the `best_playedX.csv` files: 
coming soon...

# Code overview
In this section I describe what each `.py` files does. 

coming soon...
