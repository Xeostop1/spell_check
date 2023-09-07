SELECT 
   tb_sm022_thumbs.pcs_id, 
    ISNULL(CONCAT(CAST(tb_sm022_thumbs.http AS VARCHAR), CAST(tb_sm022_thumbs.file_name AS VARCHAR)), 'NULL') AS t_url
FROM 
    tb_sm022_thumbs  
LEFT JOIN 
    TB_SM022 ON CAST(TB_SM022.dir_id AS VARCHAR) = CAST(tb_sm022_thumbs.pcs_id AS VARCHAR);