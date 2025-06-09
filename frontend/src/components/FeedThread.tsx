import React from "react";
import style from "./Thread.module.scss";
import Link from "next/link";
import { formatDistanceToNow } from "date-fns";
import ReactMarkdown from "react-markdown";
import Image from "next/image";

interface ThreadProps {
    board: string;
    board_name: string;
    id: number;
    title: string;
    text: string;
    author: string;
    replyCount: number;
    updated_at: string;
    img_upload: string | null;
    index: number;
}

const FeedThread: React.FC<ThreadProps> = ({
    board,
    board_name,
    id,
    title,
    text,
    author,
    replyCount,
    updated_at,
    img_upload,
    index,
}) => {
    const relativeTime = formatDistanceToNow(new Date(updated_at), {
        addSuffix: true,
    });

    const limitedText = text.length > 200 ? `${text.slice(0, 200)}...` : text;

    const styleToUse = index % 2 === 0 ? style.thread : `${style.thread} ${style.thread__alt}`

    return (
        <Link href={`/b/${board}/${id}`} style={{ textDecoration: "none" }}>
            <div className={styleToUse}>
                <div className={style.thread__board}>/{board}/ - {board_name}</div>
                <div className={style.thread__title}>{title}</div>
                <div className={style.thread__details}>
                    by {author} •{" "}
                    {replyCount === 0 ? "last created " : "last replied "}
                    {relativeTime} • {replyCount}{" "}
                    {replyCount === 1 ? "reply" : "replies"}
                </div>
                {img_upload && (
                    <div className={style.thread__image}>
                        <Image
                            src={`http://127.0.0.1:8000${img_upload}`}
                            alt="Thread Image"
                            layout="responsive"
                            width={400}
                            height={400}
                        />
                    </div>
                )}
                <div className={style.thread__text}>
                    <ReactMarkdown>{limitedText}</ReactMarkdown>
                </div>
            </div>
        </Link>
    );
};

export default FeedThread;
