-- LIST ALL GENRES AND NUMBER OF SHOWS LINKED TO EACH

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 1;
