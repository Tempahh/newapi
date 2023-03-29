select media.*, count(votes.media_id) as votes from media left join votes on media.id = votes.media_id group by media.id
