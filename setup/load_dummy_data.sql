CONNECT lab_admin/lab123;
BEGIN
  FOR i IN 1..10 LOOP
    INSERT INTO employees (emp_name, job_title, salary, dept_id)
    VALUES (
      'Employee_' || i,
      CASE WHEN MOD(i,3)=0 THEN 'DBA' WHEN MOD(i,3)=1 THEN 'Developer' ELSE 'Analyst' END,
      3000 + (i*500),
      MOD(i,3)+1
    );
  END LOOP;
  COMMIT;
END;
/
