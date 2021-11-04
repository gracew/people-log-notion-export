--CREATE EXTENSION pgcrypto;

CREATE TABLE if not exists people (
    id uuid primary key,
    name text not null,
    context text,
    how_i_know_them text
);

CREATE TABLE if not exists log (
    id uuid primary key default gen_random_uuid(),
    date date not null,
    hours real not null,
    type text,
    person_id uuid not null,
    constraint fk_person foreign key(person_id) references people(id)
);