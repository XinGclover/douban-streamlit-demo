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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: demo_high_rating_dramas_source_zhaoxuelu; Type: TABLE; Schema: public; Owner: cindy
--

CREATE TABLE public.demo_high_rating_dramas_source_zhaoxuelu (
    high_rating_drama_id character varying(20),
    drama_name character varying(40),
    high_rating_user_count bigint
);


ALTER TABLE public.demo_high_rating_dramas_source_zhaoxuelu OWNER TO cindy;

--
-- Name: demo_lowrating_users_distribution; Type: TABLE; Schema: public; Owner: cindy
--

CREATE TABLE public.demo_lowrating_users_distribution (
    group_id integer,
    group_name text,
    group_who text,
    user_cnt bigint
);


ALTER TABLE public.demo_lowrating_users_distribution OWNER TO cindy;

--
-- Name: demo_reply_users_distribution; Type: TABLE; Schema: public; Owner: cindy
--

CREATE TABLE public.demo_reply_users_distribution (
    user_id character varying(20),
    user_name text,
    reply_count bigint,
    rnk bigint,
    group_names text[]
);


ALTER TABLE public.demo_reply_users_distribution OWNER TO cindy;

--
-- PostgreSQL database dump complete
--

