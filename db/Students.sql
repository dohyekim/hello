PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Student (
id integer primary key autoincrement not null,
name text not null default 'aaa',
mobile text null);
INSERT INTO Student VALUES(1,'홍길동','2323-4545');
INSERT INTO Student VALUES(2,'홍길순','9876-5432');
INSERT INTO Student VALUES(3,'아아아','5432-1986');
INSERT INTO Student VALUES(4,'Eileen','1111-2222');
INSERT INTO Student VALUES(5,'김일수','9785-2748');
INSERT INTO Student VALUES(6,'김김김','2345-6789');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('Student',6);
COMMIT;
