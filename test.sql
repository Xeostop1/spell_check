sql="SELECT * FROM (SELECT ROW_NUMBER() OVER (ORDER BY "

Select Case sort 
    Case "sysdate_asc"
        sql=sql&"sysdate ASC"
    Case "sysdate_desc"
        sql=sql&"sysdate DESC"
    Case "pcs_name_asc"
        sql=sql&"pcs_name ASC"
    Case "pcs_name_desc"
        sql=sql&"pcs_name DESC"    
	'디폴트 최신순  
    Case Else 
        sql=sql&"sysdate DESC"
End Select 

'섬네일 URL + case 문에서 넘어오면 뒤쪽 쿼리로 보여주기 
sql = sql&") AS RowNum, pcs_name, sysdate, pcs_price," &
            " ISNULL(CONCAT(CAST(tb_SM22_thumbs.http AS VARCHAR), CAST(tb_SM22_thumbs.file_name AS VARCHAR)), 'NULL') as t_url "
sql = sql&" FROM tb_sm022 LEFT JOIN TB_SM22_THUMBS ON TB_SM22.pcs_id = TB_SM22_THUMBS.pcs_ID WHERE DIR_ID=" 
sql = sql& dir_id & " AND delyn='N' AND RowNum >= "& startPage

If startPage + PerPage <= totalR then
   sql=sql & "  AND index_t.RowNum < "&(startPage + PerPage)
End If
