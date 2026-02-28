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
-- Name: demo_zhaoxuelu_comments; Type: TABLE; Schema: public; Owner: cindy
--

CREATE TABLE public.demo_zhaoxuelu_comments (
    user_id character varying(20) NOT NULL,
    user_name character varying(60),
    votes integer,
    status character varying(10),
    rating integer,
    user_location character varying(20),
    create_time timestamp without time zone NOT NULL,
    user_comment text,
    insert_time timestamp without time zone DEFAULT now(),
    batch_id text
);


ALTER TABLE public.demo_zhaoxuelu_comments OWNER TO cindy;

--
-- Name: demo_zhaoxuelu_comments unique_zhaoxuelu_user_time; Type: CONSTRAINT; Schema: public; Owner: cindy
--

ALTER TABLE ONLY public.demo_zhaoxuelu_comments
    ADD CONSTRAINT unique_zhaoxuelu_user_time UNIQUE (user_id, create_time);


--
-- Name: idx_user_zhaoxuelu; Type: INDEX; Schema: public; Owner: cindy
--

CREATE INDEX idx_user_zhaoxuelu ON public.demo_zhaoxuelu_comments USING btree (user_id);


--
-- PostgreSQL database dump complete
--

