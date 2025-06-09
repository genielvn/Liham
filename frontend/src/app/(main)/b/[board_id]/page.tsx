"use client";

import { notFound } from "next/navigation";
import Thread from "@/components/Thread";
import ThreadCreate from "@/components/ThreadCreate";
import style from "./page.module.scss";
import { BoardThreadListData } from "@/types/boardthread";
import { getSelfUserData, getThreads } from "@/services/api";
import { useEffect, useState } from "react";
import { set } from "date-fns";

interface ThreadListProps {
    params: {
        board_id: string;
    };
}

export default function ThreadList({ params }: ThreadListProps) {
    const [data, setData] = useState<BoardThreadListData>();
    const [error, setError] = useState<boolean>(false);
    const [isBanned, setIsBanned] = useState<boolean>(false);
    const { board_id } = params;

    useEffect(() => {
        const fetchThreads = async () => {
            try {
                const response = await getThreads(board_id);
                setData(response.data);
            } catch (error) {
                setError(true);
            }
        };
        const fetchBanned = async () => {
            try {
                const response = await getSelfUserData();
                setIsBanned(response.data.user.is_banned);
            } catch (error) {
                setError(true);
            }
        };
        fetchBanned();
        fetchThreads();
    }, []);

    if (error) {
        return notFound();
    }

    return (
        data && (
            <>
                <h2>{data?.board.name}</h2>
                <p className={style.thread__board_description}>
                    {data?.board.description}
                </p>
                <div className={style.thread__list}>
                    {!isBanned && <ThreadCreate board={board_id} />}
                    {isBanned && (
                        <p style={{ color: "red", margin: "1rem 0" }}>
                            You are banned and cannot create threads.
                        </p>
                    )}
                    {data?.threads.map((thread, index) => (
                        <Thread
                            key={thread.id}
                            id={thread.id}
                            board={board_id}
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
