"use client";
import { notFound } from "next/navigation";
import FeedThread from "@/components/FeedThread";
import style from "./page.module.scss";
import { ThreadData } from "@/types/thread";
import { useEffect, useState } from "react";
import { getFeed } from "@/services/api";

export default function Feed() {
    const [data, setData] = useState<ThreadData[]>([]);
    const [error, setError] = useState<boolean>(false);

    useEffect(() => {
        const fetchFeed = async () => {
            try {
                const response = await getFeed();
                setData(response.data);
            } catch (error) {
                setError(true);
            }
        };
        fetchFeed();
    }, []);

    if (error) return notFound();

    return (
        data && (
            <>
                <h1>Latest</h1>
                <div className={style.thread__list}>
                    {data?.map((thread, index) => (
                        <FeedThread
                            key={thread.id}
                            id={thread.id}
                            board={thread.board}
                            board_name={thread.board_name}
                            title={thread.title}
                            text={thread.body}
                            author={thread.author}
                            replyCount={thread.reply_count}
                            updated_at={thread.updated_at}
                            img_upload={thread.img_upload}
                            index={index}
                        />
                    ))}
                </div>
            </>
        )
    );
}
