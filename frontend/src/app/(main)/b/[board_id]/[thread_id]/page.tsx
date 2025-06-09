"use client";

import React, { useEffect, useState } from "react";
import { notFound, useRouter } from "next/navigation";
import style from "./page.module.scss";
import RepliesInput from "@/components/RepliesInput";
import Reply from "@/components/Reply";
import { formatDistanceToNow } from "date-fns";
import Link from "next/link";
import Image from "next/image";
import ReactMarkdown from "react-markdown";
import { ReplyData } from "@/types/reply";
import { SingleBoardThreadData } from "@/types/boardthread";
import {
    deleteThread,
    editThread,
    getReplies,
    getSelfUserData,
    getThread,
} from "@/services/api";
import { Modal } from "@/components/Modal";

interface ThreadProps {
    params: {
        board_id: string;
        thread_id: number;
    };
}

export default function Thread({ params }: ThreadProps) {
    const { board_id, thread_id } = params;
    const [data, setData] = useState<SingleBoardThreadData | null>(null);
    const [replies, setReplies] = useState<ReplyData[] | null>(null);
    const [error, setError] = useState<boolean>(false);
    const [isBanned, setIsBanned] = useState<boolean>(false);
    const [isAdmin, setIsAdmin] = useState<boolean>(false);
    const [currentUser, setCurrentUser] = useState<string>("");
    const [isModalOpen, setIsModalOpen] = useState(false);

    useEffect(() => {
        const fetchThread = async () => {
            try {
                const response = await getThread(board_id, thread_id);
                setData(response.data);
            } catch (error) {
                setError(true);
            }
        };
        const fetchReplies = async () => {
            try {
                const response = await getReplies(board_id, thread_id);
                setReplies(response.data);
            } catch (error) {
                console.error(error);
            }
        };
        const fetchSelfDetails = async () => {
            try {
                const response = await getSelfUserData();
                setIsBanned(response.data.user.is_banned);
                setIsAdmin(response.data.user.is_admin);
                setCurrentUser(response.data.user.username);
            } catch (error) {
                setError(true);
            }
        };
        fetchSelfDetails();
        fetchThread();
        fetchReplies();
    }, []);

    const router = useRouter();
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const [beingEdited, setBeingEdited] = useState(false);
    const [editedBody, setEditedBody] = useState("");

    if (error) {
        return notFound();
    }

    const relativeTime =
        data?.thread.created_at &&
        formatDistanceToNow(new Date(data.thread.created_at as string), {
            addSuffix: true,
        });

    const handleEdit = async () => {
        if (!editedBody) {
            alert("Please enter a body.");
            return;
        }

        const formData = new FormData();
        formData.append("body", editedBody);

        try {
            await editThread(board_id, thread_id, formData);
            alert("Thread updated successfully!");
            window.location.reload();
        } catch (error) {
            console.log(error);
            alert("Something went wrong. Please try again.");
        }
    };

    const confirmDelete = () => {
        setIsModalOpen(true);
    };

    const handleDelete = async () => {
        try {
            await deleteThread(board_id, thread_id);
            window.location.href = `/b/${board_id}`;
        } catch (error) {
            alert("Something went wrong. Please try again.");
        } finally {
            setIsModalOpen(false);
        }
    };

    return (
        data && (
            <>
                <div className={`margin-bottom-10 ${style.thread__nav}`}>
                    <button
                        onClick={() => router.back()}
                        className="btn-small btn-pink"
                    >
                        ← Back
                    </button>
                    <Link
                        className={`subheader margin-left-5 ${style.thread__subheader}`}
                        href={`/b/${data?.board.board_id}`}
                    >
                        /{data?.board.board_id}/ - {data?.board.name}
                    </Link>
                </div>
                <div className={style.thread__header}>
                    <h2 className={style.thread__title}>
                        {data?.thread.title}
                    </h2>
                    {(data?.thread.author === currentUser || isAdmin) && (
                        <div className={style.thread__dropdown}>
                            <div className={style.thread__dropdown_button}>
                                <i
                                    onClick={() =>
                                        setIsDropdownOpen((prev) => !prev)
                                    }
                                    className="bi bi-three-dots"
                                ></i>
                            </div>
                            {isDropdownOpen && (
                                <div className={style.thread__dropdown_menu}>
                                    {!isBanned && (
                                        <div
                                            className={
                                                style.thread__dropdown_item
                                            }
                                            onClick={() => {
                                                setBeingEdited(true);
                                                setEditedBody(
                                                    data?.thread.body || ""
                                                );
                                                setIsDropdownOpen(false);
                                            }}
                                        >
                                            Edit
                                        </div>
                                    )}

                                    <div
                                        className={style.thread__dropdown_item}
                                        onClick={confirmDelete}
                                    >
                                        Delete
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </div>
                <div className={style.thread__details}>
                    by{" "}
                    {data?.thread.author === "Anonymous" ? (
                        <span>{data?.thread.author}</span>
                    ) : (
                        <Link href={`/u/${data?.thread.author}`}>
                            {data?.thread.author}
                        </Link>
                    )}{" "}
                    • posted {relativeTime}
                </div>

                {beingEdited ? (
                    <div className={style.thread__text}>
                        <textarea
                            value={editedBody}
                            onChange={(e) => setEditedBody(e.target.value)}
                        />
                        <button
                            className="btn-small btn-pink"
                            onClick={handleEdit}
                        >
                            Save
                        </button>
                        <button
                            className="btn-small btn-pink"
                            onClick={() => setBeingEdited(false)}
                        >
                            Cancel
                        </button>
                    </div>
                ) : (
                    <div className={style.thread__text}>
                        <ReactMarkdown>{data?.thread.body || ""}</ReactMarkdown>
                    </div>
                )}

                {data?.thread.img_upload && (
                    <div className={style.thread__image}>
                        <Image
                            src={`http://127.0.0.1:8000${data.thread.img_upload}`}
                            alt="Thread Image"
                            layout="responsive"
                            width={400}
                            height={400}
                        />
                    </div>
                )}
                {!isBanned ? (
                    !beingEdited && (
                        <RepliesInput
                            board_id={board_id}
                            thread_id={thread_id}
                        />
                    )
                ) : (
                    <p style={{ color: "red", margin: "1rem 0" }}>
                        You are banned and cannot post replies.
                    </p>
                )}

                <h3 style={{ marginTop: "1em" }}>Replies</h3>
                {replies?.length === 0
                    ? "No replies yet"
                    : replies?.map((reply) => (
                          <Reply
                              key={reply.id}
                              id={reply.id}
                              author={reply.author}
                              content={reply.body}
                              created_at={reply.created_at}
                              img_upload={reply.img_upload}
                              is_admin={isAdmin}
                              current_user={currentUser}
                          />
                      ))}
                {isModalOpen && (
                    <Modal
                        title="Confirm Deletion"
                        content="Are you sure you want to delete this thread? This action cannot be undone."
                        okayAction={handleDelete}
                        cancelAction={() => setIsModalOpen(false)}
                        okayText="Delete"
                        cancelText="Cancel"
                        type="warning"
                    />
                )}
            </>
        )
    );
}
