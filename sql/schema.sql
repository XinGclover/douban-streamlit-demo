--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9 (Homebrew)
-- Dumped by pg_dump version 16.9 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP TABLE IF EXISTS public.demo_reply_users_distribution;
DROP TABLE IF EXISTS public.demo_member_groups;
DROP TABLE IF EXISTS public.demo_lowrating_users_distribution;
DROP TABLE IF EXISTS public.demo_high_rating_dramas_source_zhaoxuelu;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: demo_high_rating_dramas_source_zhaoxuelu; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.demo_high_rating_dramas_source_zhaoxuelu (
    high_rating_drama_id character varying(20),
    drama_name character varying(40),
    high_rating_user_count bigint
);


--
-- Name: demo_lowrating_users_distribution; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.demo_lowrating_users_distribution (
    group_id integer,
    group_name text,
    group_who text,
    user_cnt bigint
);


--
-- Name: demo_member_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.demo_member_groups (
    member_id character varying(20),
    member_name text,
    group_names text[],
    group_whos text[]
);


--
-- Name: demo_reply_users_distribution; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.demo_reply_users_distribution (
    user_id character varying(20),
    user_name text,
    reply_count bigint,
    rnk bigint,
    group_names text[],
    group_whos text[]
);


--
-- PostgreSQL database dump complete
--

